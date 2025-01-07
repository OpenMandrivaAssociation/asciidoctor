Name:		asciidoctor
Version:	2.0.23
Release:	2
Summary:	Tool to convert AsciiDoc(tor) text files to DocBook, HTML or Unix man pages
License:	GPLv2+
Group:		Publishing
Url:		https://asciidoctor.org/
Source0:	https://github.com/asciidoctor/asciidoctor/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	ruby
BuildRequires:	rubygems
Requires:	ruby
BuildArch:	noarch

%description
AsciiDoctor is a text document format for writing short documents, articles,
books and UNIX man pages.

%prep
%autosetup -p1

%build
ln -s asciidoctor.gemspec asciidoctor-%{version}.gemspec
mkdir build
cd build
%gem_build

%install
cd build
%gem_install
cd ..

# The gem install mechanism seems to be broken, so let's
# do it manually
mkdir -p %{buildroot}%{ruby_vendorlibdir}
cp -a lib/* %{buildroot}%{ruby_vendorlibdir}/
# FIXME this is plain wrong, but some stuff (e.g. icewm)
# hardcodes this bogus location because it's what other
# distros do
cp -a data %{buildroot}%{ruby_vendorlibdir}/..
cp -a bin %{buildroot}%{_prefix}

%files
%{_bindir}/asciidoctor
%{ruby_vendorlibdir}/asciidoctor.rb
%{ruby_vendorlibdir}/asciidoctor
%{ruby_vendorlibdir}/../data
%{ruby_gemdir}/cache/*
%optional %{ruby_gemdir}/doc/*
%{ruby_gemdir}/specifications/*
