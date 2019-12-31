Name:       Judy
Version:    1.0.5
Release:    19
Summary:    C library array
License:    LGPLv2+
URL:        http://sourceforge.net/projects/judy/
Source0:    http://downloads.sf.net/judy/Judy-%{version}.tar.gz

Patch0000:  Judy-1.0.4-test-shared.patch
Patch0001:  Judy-1.0.4-fix-Judy1-mans.patch
Patch0002:  Judy-1.0.5-undefined-behavior.patch

BuildRequires: coreutils gawk make sed gcc >= 4.1

%description
The package provides the most advanced core technology, the main
advantages are scalability, high performance and memory efficiency.

%package devel
Summary:    Development libraries and headers for Judy
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains header files and development libraries.

%package          help
Summary:          API documentation for Judy.

%description      help
The help for Judy to use.

%prep
%autosetup -n judy-%{version} -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -fno-tree-ccp -fno-tree-dominator-opts -fno-tree-copy-prop -fno-tree-vrp"
%configure --disable-static

make

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.a
%delete_la
rm -rf doc/man doc/Makefile* doc/ext/{README_deliver,COPYRIGHT,LICENSE}

%check
cd test
./Checkit
cd -

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%license COPYING
%{_libdir}/libJudy.so.*

%files devel
%{_includedir}/Judy.h
%{_libdir}/libJudy.so

%files help
%{_mandir}/man3/J*.3*
%doc README examples

%changelog
* Thu Nov 14 2019 wangye<wangye54@huawei.com> - 1.0.5-19
- Package init
