%{?scl:%scl_package nodejs-readdir-scoped-modules}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-readdir-scoped-modules

%global npm_name readdir-scoped-modules
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-readdir-scoped-modules
Version:	1.0.2
Release:	2%{?dist}
Summary:	Like `fs.readdir` but handling `@org/module` dirs as if they were a single entry.
Url:		https://github.com/npm/readdir-scoped-modules
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

BuildRequires:	%{?scl_prefix}npm(debuglog)
BuildRequires:	%{?scl_prefix}npm(dezalgo)
BuildRequires:	%{?scl_prefix}npm(graceful-fs)
BuildRequires:	%{?scl_prefix}npm(once)

Requires:	%{?scl_prefix}npm(debuglog)
Requires:	%{?scl_prefix}npm(dezalgo)
Requires:	%{?scl_prefix}npm(graceful-fs)
Requires:	%{?scl_prefix}npm(once)

%description
Like `fs.readdir` but handling `@org/module` dirs as if they were a single entry.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/readdir-scoped-modules

%doc README.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-1
- Initial build
