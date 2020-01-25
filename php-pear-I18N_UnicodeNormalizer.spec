# TODO:
#  - pl description cleanups
%define		_class		I18N
%define		_subclass	UnicodeNormalizer
%define		_status		stable
%define		_pearname	I18N_UnicodeNormalizer
Summary:	%{_pearname} - Unicode Normalizer
Summary(pl.UTF-8):	%{_pearname} - normalizator Unicode
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	5
License:	The BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5dbeae8800105e9e1f948c061b33aeb8
Patch0:		%{name}-paths_fix.patch
URL:		http://pear.php.net/package/I18N_UnicodeNormalizer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-22
Suggests:	php-pear-PEAR
Obsoletes:	php-pear-I18N_UnicodeNormalizer-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(PEAR.*)

%description
"...Unicode's normalization is the concept of character composition
and decomposition.

Character composition is the process of combining simpler characters
into fewer precomposed characters, such as the n character and the
combining ~ character into the single n+~ character. Decomposition is
the opposite process, breaking precomposed characters back into their
component pieces...

...Normalization is important when comparing text strings for
searching and sorting (collation)..." [Wikipedia]

Performs the 4 normalizations:

NFD: Canonical Decomposition NFC: Canonical Decomposition, followed by
Canonical Composition NFKD: Compatibility Decomposition NFKC:
Compatibility Decomposition, followed by Canonical Composition

Complies with the official Unicode.org regression test.

Uses UTF8 binary strings natively but can normalize a string in any
UTF format.

Fully tested with phpUnit. Code coverage test close to 100%.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
"... normalizacja Unicode to określenie dla (de)kompozycji znaków
Unicode.

Kompozycja znaku to proces łączenia prostych znaków w mniejszą liczbę
złożonych, przykładowo znak n oraz ~ w pojedynczy n+~. Dekompozycja to
proces odwrotny, podział połączonych znaków w części składowe...

... normalizacja jest istotna w przypadku porównywania tekstów w celu
wyszukiwania oraz sortowania..."

[Wikipedia]

Istnieją 4 rodzaje normalizacji: NFD: Kanoniczna dekompozycja, NFC:
kanoniczna dekompozycja wraz z kanoniczną kompozycją, NKFD:
kompatybilna dekompozycja, NKFS: kompatybilna dekompozycja wraz z
kanoniczną kompozycją.

Pakiet ten przechodzi testy oficjalnego zestawu Unicode.org.

W pełni przetestowane za pomocą phpUnit. Pokrycie kodu bliskie 100%.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt docs/I18N_UnicodeNormalizer/docs/examples.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/I18N/UnicodeNormalizer
%{php_pear_dir}/I18N/UnicodeNormalizer.php
%{php_pear_dir}/data/I18N_UnicodeNormalizer
