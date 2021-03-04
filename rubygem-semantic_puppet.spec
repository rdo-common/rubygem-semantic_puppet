# Generated from semantic_puppet-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name semantic_puppet

Name: rubygem-%{gem_name}
Version: 1.0.2
Release: 2%{?dist}
Summary: Useful tools for working with Semantic Versions
License: ASL 2.0
URL: https://github.com/puppetlabs/semantic_puppet
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
# for testing
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Tools used by Puppet to parse, validate, and compare Semantic Versions and
Version Ranges and to query and resolve module dependencies.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.rubocop.yml,.travis.yml,.yardopts}

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/appveyor.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/semantic_puppet.gemspec
%{gem_instdir}/spec

%changelog
* Thu Mar 4 2021 Alfredo Moralejo <amoralej@redhat.com> - 1.0.2-2
- Rebuild in RDO for CentOS8.

* Mon May 4 2020 Breno Brand Fernandes <brandfbb@gmail.com> - 1.0.2-1
- First build
