/**
 * @brief MAVROS GCS proxy
 * @file gcs_bridge.cpp
 * @author Vladimir Ermakov <vooon341@gmail.com>
 */
/*
 * Copyright 2014 Vladimir Ermakov.
 *
 * This file is part of the mavros package and subject to the license terms
 * in the top-level LICENSE file of the mavros repository.
 * https://github.com/mavlink/mavros/tree/master/LICENSE.md
 */

#include <ros/ros.h>
#include <ros/console.h>

#include <mavros/utils.h>
#include <mavconn/interface.h>

#include <mavros/Mavlink.h>

using namespace mavros;
using namespace mavconn;

ros::Publisher mavlink_pub;
ros::Subscriber mavlink_sub;
MAVConnInterface::Ptr gcs_link;

void mavlink_pub_cb(const mavlink_message_t *mmsg, uint8_t sysid, uint8_t compid) {
	MavlinkPtr rmsg = boost::make_shared<Mavlink>();

	rmsg->header.stamp = ros::Time::now();
	mavutils::copy_mavlink_to_ros(mmsg, rmsg);
	mavlink_pub.publish(rmsg);
};

void mavlink_sub_cb(const Mavlink::ConstPtr &rmsg) {
	mavlink_message_t mmsg;

	if (mavutils::copy_ros_to_mavlink(rmsg, mmsg))
		gcs_link->send_message(&mmsg, rmsg->sysid, rmsg->compid);
	else
		ROS_ERROR("Packet drop: illegal payload64 size");
};

int main(int argc, char *argv[])
{
	ros::init(argc, argv, "gcs_bridge");
	ros::NodeHandle priv_nh("~");
	ros::NodeHandle mavlink_nh("/mavlink");

	std::string gcs_url;
	priv_nh.param<std::string>("gcs_url", gcs_url, "udp://@");

	try {
		gcs_link = MAVConnInterface::open_url(gcs_url);
	}
	catch (mavconn::DeviceError &ex) {
		ROS_FATAL("GCS: %s", ex.what());
		return 1;
	}

	mavlink_pub = mavlink_nh.advertise<Mavlink>("to", 10);
	gcs_link->message_received.connect(mavlink_pub_cb);

	mavlink_sub = mavlink_nh.subscribe("from", 10, mavlink_sub_cb,
		ros::TransportHints()
			.unreliable()
			.maxDatagramSize(1024));

	ros::spin();
	return 0;
}

