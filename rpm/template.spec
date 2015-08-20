Name:           ros-jade-mavros
Version:        0.14.2
Release:        0%{?dist}
Summary:        ROS mavros package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-diagnostic-updater
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-libmavconn
Requires:       ros-jade-mavlink
Requires:       ros-jade-mavros-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-pluginlib
Requires:       ros-jade-rosconsole-bridge
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospy
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-tf2-ros
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-jade-angles
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-libmavconn
BuildRequires:  ros-jade-mavlink
BuildRequires:  ros-jade-mavros-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-rosconsole-bridge
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-tf2-ros

%description
MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground
Control Station.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Aug 20 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.1-0
- Autogenerated by Bloom

* Mon Aug 17 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.0-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.13.1-0
- Autogenerated by Bloom

* Sat Aug 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

* Wed Jul 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.12.0-0
- Autogenerated by Bloom

* Sun Apr 26 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.2-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue Mar 24 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.0-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.2-0
- Autogenerated by Bloom

