Name:           ros-hydro-mavros-extras
Version:        0.8.6
Release:        0%{?dist}
Summary:        ROS mavros_extras package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_extras
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-mavlink
Requires:       ros-hydro-mavros
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-mavlink
BuildRequires:  ros-hydro-mavros
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs

%description
Extra nodes and plugins for mavros

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Mar 04 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.8.6-0
- Autogenerated by Bloom

* Tue Nov 04 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.8.5-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.8.4-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.8.3-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.8.2-0
- Autogenerated by Bloom

* Sun Nov 02 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.8.1-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.8.0-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.7.1-0
- Autogenerated by Bloom

* Tue Aug 12 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.7.0-0
- Autogenerated by Bloom

