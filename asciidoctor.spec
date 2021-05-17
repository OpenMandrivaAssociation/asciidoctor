Name:		asciidoctor
Version:	2.0.15
Release:	1
Summary:	Tool to convert AsciiDoc(tor) text files to DocBook, HTML or Unix man pages
License:	GPLv2+
Group:		Publishing
Url:		http://asciidoctor.org/
Source0:	https://github.com/asciidoctor/asciidoctor/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	ruby
BuildRequires:	rubygems
BuildArch:	noarch

%description
AsciiDoctor is a text document format for writing short documents, articles,
books and UNIX man pages.

%prep
%autosetup -p1

%build
gem build %{name}.gemspec

%install
%gem_install -n %{name}-%{version}.gem -d %{buildroot}

%files
%{_bindir}/asciidoctor
%{_libdir}/ruby/gems/*/cache/asciidoctor-%{version}.gem
%{_libdir}/ruby/gems/*/doc/asciidoctor-%{version}
%{_libdir}/ruby/gems/*/gems/asciidoctor-%{version}
%{_libdir}/ruby/gems/*/specifications/asciidoctor-%{version}.gemspec
