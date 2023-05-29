- install
	- https://litterhougelangley.club/blog/2021/05/21/gentoo/
	- https://bitbili.net/gentoo-linux-installation-and-usage-tutorial.html
	- make.config
		- ```bash
		  # These settings were set by the catalyst build script that automatically
		  # built this stage.
		  # Please consult /usr/share/portage/config/make.conf.example for a more
		  # detailed example.
		  COMMON_FLAGS="-march=sandybridge -O2 -pipe"
		  CFLAGS="${COMMON_FLAGS}"
		  CXXFLAGS="${COMMON_FLAGS}"
		  FCFLAGS="${COMMON_FLAGS}"
		  FFLAGS="${COMMON_FLAGS}"
		  CPU_FLAGS_X86="mmx mmxext sse sse2 sse3"
		  
		  # NOTE: This stage was built with the bindist Use flag enabled
		  PORTDIR="/var/db/repos/gentoo"
		  DISTDIR="/var/cache/distfiles"
		  PKGDIR="/var/cache/binpkgs"
		  
		  # This sets the language of build output to English.
		  # Please keep this setting intact when reporting bugs.
		  LC_MESSAGES=C
		  MAKEOPTS="-j16"
		  GENTOO_MIRRORS="https://mirrors.ustc.edu.cn/gentoo/"
		  EMERGE_DEFAULT_OPTS="--keep-going --with-bdeps=y --autounmask-write=y --quiet-build=y -j -l"
		  ACCEPT_LICENSE="*"
		  L10N="en-US zh-CN en zh"
		  LINGUAS="en_US zh_CN en zh"
		  RUBY_TARGETS="ruby30"
		  FEATURES="ccache"
		  CCACHE_DIR="/var/cache/ccache"
		  
		  CC="clang"
		  CXX="clang++"
		  AR="llvm-ar"
		  NM="llvm-nm"
		  RANLIB="llvm-ranlib"
		  
		  LDFLAGS="${LDFLAGS} -fuse-ld=lld -rtlib=compiler-rt -unwindlib=libunwind -Wl,--as-needed"
		  ```