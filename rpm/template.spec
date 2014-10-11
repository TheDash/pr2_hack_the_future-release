Name:           ros-hydro-program-queue
Version:        1.0.7
Release:        0%{?dist}
Summary:        ROS program_queue package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/program_queue
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-hack-the-web-program-executor
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-rospy
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-std-srvs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-hack-the-web-program-executor
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-std-srvs

%description
program_queue

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Oct 11 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.7-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Austin Hendrix <ahrendrix@willowgarage.com> - 1.0.5-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Austin Hendrix <ahrendrix@willowgarage.com> - 1.0.3-0
- Autogenerated by Bloom

