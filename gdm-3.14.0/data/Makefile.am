NULL =
EXTRA_DIST =

SUBDIRS =			\
	applications		\
	autostart		\
	pixmaps			\
	$(NULL)

initdir = $(gdmconfdir)/Init
postdir = $(gdmconfdir)/PostSession
predir = $(gdmconfdir)/PreSession
primedir = $(gdmconfdir)/Prime
primeoffdir = $(gdmconfdir)/PrimeOff
postlogindir = $(gdmconfdir)/PostLogin
workingdir = $(GDM_WORKING_DIR)
xauthdir = $(GDM_XAUTH_DIR)
screenshotdir = $(GDM_SCREENSHOT_DIR)
cachedir = $(localstatedir)/cache/gdm

Xsession: $(srcdir)/Xsession.in
	sed	-e 's,[@]XSESSION_SHELL[@],$(XSESSION_SHELL),g' \
		-e 's,[@]libexecdir[@],$(libexecdir),g' \
		<$(srcdir)/Xsession.in >Xsession

Init: $(srcdir)/Init.in
	sed	-e 's,[@]X_PATH[@],$(X_PATH),g' \
		<$(srcdir)/Init.in >Init

PreSession: $(srcdir)/PreSession.in
	sed	-e 's,[@]X_PATH[@],$(X_PATH),g' \
		<$(srcdir)/PreSession.in >PreSession
PostSession: $(srcdir)/PostSession.in
	sed	-e 's,[@]X_PATH[@],$(X_PATH),g' \
		<$(srcdir)/PostSession.in >PostSession

gdm.conf-custom: $(srcdir)/gdm.conf-custom.in
	sed	-e 's,[@]GDM_DEFAULTS_CONF[@],$(GDM_DEFAULTS_CONF),g' \
		<$(srcdir)/gdm.conf-custom.in >gdm.conf-custom

dbusconfdir = $(DBUS_SYS_DIR)
dbusconf_in_files = gdm.conf.in
dbusconf_DATA = $(dbusconf_in_files:.conf.in=.conf)

@INTLTOOL_SCHEMAS_RULE@
@INTLTOOL_XML_NOMERGE_RULE@

# dconf database and profile
dconf_db_files = \
	dconf/defaults/00-upstream-settings		\
	dconf/defaults/locks/00-upstream-settings-locks

dconfdbdir = $(pkgdatadir)
dconfdb_DATA = greeter-dconf-defaults
greeter-dconf-defaults: $(dconf_db_files)
	$(AM_V_GEN) dconf compile $@ $(srcdir)/dconf/defaults

dconfprofiledir = $(DATADIR)/dconf/profile
dconfprofile_DATA = dconf/gdm

gsettings_SCHEMAS = org.gnome.login-screen.gschema.xml
@GSETTINGS_RULES@

schemasdir = $(pkgdatadir)
schemas_in_files = gdm.schemas.in
schemas_DATA = $(schemas_in_files:.schemas.in=.schemas)

gdm.schemas.in: $(srcdir)/gdm.schemas.in.in
	sed	-e 's,[@]GDMPREFETCHCMD[@],$(GDMPREFETCHCMD),g' \
		-e 's,[@]GDM_CUSTOM_CONF[@],$(GDM_CUSTOM_CONF),g' \
		-e 's,[@]GDM_USER_PATH[@],$(GDM_USER_PATH),g' \
		-e 's,[@]GDM_USERNAME[@],$(GDM_USERNAME),g' \
		-e 's,[@]GDM_GROUPNAME[@],$(GDM_GROUPNAME),g' \
		-e 's,[@]HALT_COMMAND[@],$(HALT_COMMAND),g' \
		-e 's,[@]REBOOT_COMMAND[@],$(REBOOT_COMMAND),g' \
		-e 's,[@]SOUND_PROGRAM[@],$(SOUND_PROGRAM),g' \
		-e 's,[@]SUSPEND_COMMAND[@],$(SUSPEND_COMMAND),g' \
		-e 's,[@]XEVIE_OPTION[@],$(XEVIE_OPTION),g' \
		-e 's,[@]ALWAYS_RESTART_SERVER[@],$(ALWAYS_RESTART_SERVER),g' \
		-e 's,[@]X_CONFIG_OPTIONS[@],$(X_CONFIG_OPTIONS),g' \
		-e 's,[@]X_SERVER[@],$(X_SERVER),g' \
		-e 's,[@]X_XNEST_CMD[@],$(X_XNEST_CMD),g' \
		-e 's,[@]X_XNEST_CONFIG_OPTIONS[@],$(X_XNEST_CONFIG_OPTIONS),g' \
		-e 's,[@]X_XNEST_UNSCALED_FONTPATH[@],$(X_XNEST_UNSCALED_FONTPATH),g' \
		-e 's,[@]GDM_RBAC_SYSCMD_KEYS[@],$(GDM_RBAC_SYSCMD_KEYS),g' \
		-e 's,[@]datadir[@],$(datadir),g' \
		-e 's,[@]gdmconfdir[@],$(gdmconfdir),g' \
		-e 's,[@]libdir[@],$(libdir),g' \
		-e 's,[@]libexecdir[@],$(libexecdir),g' \
		-e 's,[@]gdmlocaledir[@],$(gdmlocaledir),g' \
		-e 's,[@]logdir[@],$(logdir),g' \
		-e 's,[@]pixmapdir[@],$(pixmapdir),g' \
		-e 's,[@]sbindir[@],$(sbindir),g' \
		<$(srcdir)/gdm.schemas.in.in >gdm.schemas.in

EXTRA_DIST += gdm-shell.session.in

gdm-shell.session: $(srcdir)/gdm-shell.session.in
	sed	-e 's,[@]libexecdir[@],$(libexecdir),g' \
		-e 's,[@]CHECK_ACCELERATED_DIR[@],$(CHECK_ACCELERATED_DIR),g' \
		< $< > $@.tmp && mv $@.tmp $@

localealiasdir = $(datadir)/gdm
localealias_DATA = locale.alias

sessiondir = $(datadir)/gnome-session/sessions
session_DATA =  gdm-shell.session

pam_redhat_files = pam-redhat/gdm.pam		\
	pam-redhat/gdm-autologin.pam		\
	pam-redhat/gdm-launch-environment.pam	\
	pam-redhat/gdm-fingerprint.pam		\
	pam-redhat/gdm-smartcard.pam		\
	pam-redhat/gdm-password.pam		\
	pam-redhat/gdm-pin.pam			\
	$(NULL)
EXTRA_DIST += $(pam_redhat_files)

pam_openembedded_files = pam-openembedded/gdm.pam	\
	pam-openembedded/gdm-autologin.pam		\
	pam-openembedded/gdm-launch-environment.pam	\
	pam-openembedded/gdm-pin.pam			\
	$(NULL)
EXTRA_DIST += $(pam_openembedded_files)

pam_exherbo_files = pam-exherbo/gdm-autologin.pam \
	pam-exherbo/gdm-launch-environment.pam	 \
	pam-exherbo/gdm-fingerprint.pam	         \
	pam-exherbo/gdm-smartcard.pam            \
	pam-exherbo/gdm-password.pam             \
	pam-exherbo/gdm-pin.pam	                 \
	$(NULL)
EXTRA_DIST += $(pam_exherbo_files)

pam_lfs_files = pam-lfs/gdm.pam			\
	pam-lfs/gdm-autologin.pam		\
	pam-lfs/gdm-launch-environment.pam	\
	pam-lfs/gdm-fingerprint.pam		\
	pam-lfs/gdm-smartcard.pam		\
	pam-lfs/gdm-password.pam		\
	pam-lfs/gdm-pin.pam			\
	$(NULL)
EXTRA_DIST += $(pam_lfs_files)

if ENABLE_REDHAT_PAM_CONFIG
pam_files = $(pam_redhat_files)
endif
if ENABLE_OPENEMBEDDED_PAM_CONFIG
pam_files = $(pam_openembedded_files)
endif
if ENABLE_EXHERBO_PAM_CONFIG
pam_files = $(pam_exherbo_files)
endif
if ENABLE_LFS_PAM_CONFIG
pam_files = $(pam_lfs_files)
endif

EXTRA_DIST +=			\
	$(dconf_db_files)	\
	$(schemas_in_files)	\
	$(schemas_DATA)		\
	$(dbusconf_in_files)	\
	$(localealias_DATA)	\
	gdm.schemas.in.in	\
	gdm.conf-custom.in 	\
	Xsession.in 		\
	Init.in 		\
	PreSession.in 		\
	Prime			\
    PrimeOff        \
	PostSession.in 		\
	PostLogin 		\
	org.gnome.login-screen.gschema.xml.in \
	$(NULL)

CLEANFILES = 				\
	Xsession			\
	gdm.conf-custom			\
	Init				\
	PreSession			\
	PostSession			\
	$(gsettings_SCHEMAS)		\
	greeter-dconf-defaults		\
	$(NULL)

DISTCLEANFILES =			\
	$(dbusconf_DATA)		\
	gdm-shell.session		\
	gdm.schemas			\
	$(NULL)

MAINTAINERCLEANFILES =			\
	*~				\
	Makefile.in

systemdsystemunit =

if HAVE_SYSTEMD

gdm.service: $(srcdir)/gdm.service.in
	$(AM_V_GEN)sed \
		-e 's,[@]sbindir[@],$(sbindir),g' \
		-e 's,[@]GDM_INITIAL_VT[@],$(GDM_INITIAL_VT),g' \
		< $< > $@
systemdsystemunit += gdm.service
CLEANFILES += gdm.service

endif

EXTRA_DIST += gdm.service.in

uninstall-hook:
	rm -f \
	$(DESTDIR)$(GDM_CUSTOM_CONF) \
	$(DESTDIR)$(gdmconfdir)/Xsession \
	$(DESTDIR)$(initdir)/Default \
	$(DESTDIR)$(postlogindir)/Default.sample \
	$(DESTDIR)$(predir)/Default \
	$(DESTDIR)$(primedir)/Default \
	$(DESTDIR)$(primeoffdir)/Default \
	$(DESTDIR)$(postdir)/Default \
	$(DESTDIR)$(sysconfdir)/dconf/db/gdm \
	$(DESTDIR)$(sysconfdir)/dconf/profile/gdm \
	-rf \
	$(DESTDIR)$(screenshotdir) \
	$(DESTDIR)$(xauthdir) \
	$(DESTDIR)$(PAM_PREFIX)/pam.d

	if test -n "$(systemdsystemunit)"; then \
		rm -f $(DESTDIR)$(SYSTEMD_SYSTEM_UNIT_DIR)/$(systemdsystemunit); \
		rmdir $(DESTDIR)$(SYSTEMD_SYSTEM_UNIT_DIR) || : ; \
	fi


install-data-hook: gdm.conf-custom Xsession Init PostSession PreSession $(systemdsystemunit)
	if test '!' -d $(DESTDIR)$(gdmconfdir); then \
		$(mkinstalldirs) $(DESTDIR)$(gdmconfdir); \
		chmod 755 $(DESTDIR)$(gdmconfdir); \
	fi
	if test '!' -f $(DESTDIR)$(GDM_CUSTOM_CONF); then \
		$(INSTALL_DATA) gdm.conf-custom $(DESTDIR)$(GDM_CUSTOM_CONF); \
		chmod 644 $(DESTDIR)$(GDM_CUSTOM_CONF); \
	fi

	$(INSTALL_SCRIPT) Xsession $(DESTDIR)$(gdmconfdir)/Xsession

	if test '!' -d $(DESTDIR)$(initdir); then \
		$(mkinstalldirs) $(DESTDIR)$(initdir); \
		chmod 755 $(DESTDIR)$(initdir); \
	fi
	-if test -f $(DESTDIR)$(initdir)/Default; then \
		cp -f $(DESTDIR)$(initdir)/Default $(DESTDIR)$(initdir)/Default.orig; \
	fi
	$(INSTALL_SCRIPT) Init $(DESTDIR)$(initdir)/Default

	if test '!' -d $(DESTDIR)$(postlogindir); then \
		$(mkinstalldirs) $(DESTDIR)$(postlogindir); \
		chmod 755 $(DESTDIR)$(postlogindir); \
	fi
	$(INSTALL_SCRIPT) $(srcdir)/PostLogin $(DESTDIR)$(postlogindir)/Default.sample

	if test '!' -d $(DESTDIR)$(predir); then \
		$(mkinstalldirs) $(DESTDIR)$(predir); \
		chmod 755 $(DESTDIR)$(predir); \
	fi
	-if test -f $(DESTDIR)$(predir)/Default; then \
		cp -f $(DESTDIR)$(predir)/Default $(DESTDIR)$(predir)/Default.orig; \
	fi
	$(INSTALL_SCRIPT) PreSession $(DESTDIR)$(predir)/Default

	if test '!' -d $(DESTDIR)$(primedir); then \
		$(mkinstalldirs) $(DESTDIR)$(primedir); \
		chmod 755 $(DESTDIR)$(primedir); \
	fi
	-if test -f $(DESTDIR)$(primedir)/Default; then \
		cp -f $(DESTDIR)$(primedir)/Default $(DESTDIR)$(primedir)/Default.orig; \
	fi
	$(INSTALL_SCRIPT) Prime $(DESTDIR)$(primedir)/Default

	if test '!' -d $(DESTDIR)$(primeoffdir); then \
		$(mkinstalldirs) $(DESTDIR)$(primeoffdir); \
		chmod 755 $(DESTDIR)$(primeoffdir); \
	fi
	-if test -f $(DESTDIR)$(primeoffdir)/Default; then \
		cp -f $(DESTDIR)$(primeoffdir)/Default $(DESTDIR)$(primeoffdir)/Default.orig; \
	fi
	$(INSTALL_SCRIPT) PrimeOff $(DESTDIR)$(primeoffdir)/Default

	if test '!' -d $(DESTDIR)$(postdir); then \
		$(mkinstalldirs) $(DESTDIR)$(postdir); \
		chmod 755 $(DESTDIR)$(postdir); \
	fi
	-if test -f $(DESTDIR)$(postdir)/Default; then \
		cp -f $(DESTDIR)$(postdir)/Default $(DESTDIR)$(postdir)/Default.orig; \
	fi
	$(INSTALL_SCRIPT) PostSession $(DESTDIR)$(postdir)/Default

	if test '!' -d $(DESTDIR)$(logdir); then \
		$(mkinstalldirs) $(DESTDIR)$(logdir); \
		chmod 755 $(DESTDIR)$(logdir); \
		chown root:root $(DESTDIR)$(logdir) || : ; \
	fi

	system=`uname`; \
	if test -f /usr/include/security/pam_appl.h; then \
	  if test '!' -d $(DESTDIR)$(PAM_PREFIX)/pam.d; then \
		$(mkinstalldirs) $(DESTDIR)$(PAM_PREFIX)/pam.d; \
		chmod 755 $(DESTDIR)$(PAM_PREFIX)/pam.d; \
	   fi; \
	   if test $$system = Linux; then \
	     for pamfile in $(pam_files); do \
	       bn=$$(basename $$pamfile .pam); \
	       $(INSTALL_DATA) $(srcdir)/$$pamfile $(DESTDIR)$(PAM_PREFIX)/pam.d/$$bn; \
	     done; \
	   fi; \
	   if test $$system = SunOS; then \
		echo "Please add PAM authentication for gdm, gdm-autologin and gdm-welcome in $(PAM_PREFIX)/pam.conf!"; \
	   fi; \
	fi

	if test '!' -d $(DESTDIR)$(xauthdir); then \
		$(mkinstalldirs) $(DESTDIR)$(xauthdir); \
		chmod 0711 $(DESTDIR)$(xauthdir); \
		chown root:gdm $(DESTDIR)$(xauthdir) || : ; \
	fi

	if test -n "$(systemdsystemunit)" -a '!' -d $(DESTDIR)$(SYSTEMD_SYSTEM_UNIT_DIR); then \
		$(mkinstalldirs) $(DESTDIR)$(SYSTEMD_SYSTEM_UNIT_DIR); \
		chmod 0755 $(DESTDIR)$(SYSTEMD_SYSTEM_UNIT_DIR); \
		chown root:root $(DESTDIR)$(SYSTEMD_SYSTEM_UNIT_DIR) || : ; \
		$(INSTALL_DATA) $(builddir)/$(systemdsystemunit) $(DESTDIR)$(SYSTEMD_SYSTEM_UNIT_DIR)/$(systemdsystemunit); \
	fi

	if test '!' -d $(DESTDIR)$(screenshotdir); then \
		$(mkinstalldirs) $(DESTDIR)$(screenshotdir); \
		chmod 0755 $(DESTDIR)$(screenshotdir); \
		chown gdm:gdm $(DESTDIR)$(screenshotdir) || : ; \
	fi

	if test '!' -d $(DESTDIR)$(workingdir); then \
		$(mkinstalldirs) $(DESTDIR)$(workingdir); \
		chmod 1770 $(DESTDIR)$(workingdir); \
		chown root:gdm $(DESTDIR)$(workingdir) || : ; \
	fi

	if test '!' -d $(DESTDIR)$(workingdir)/.local/share/applications; then \
		$(mkinstalldirs) $(DESTDIR)$(workingdir)/.local/share/applications; \
		chmod 0755 $(DESTDIR)$(workingdir)/.local/share/applications; \
		chown gdm:gdm $(DESTDIR)$(workingdir)/.local/share/applications || : ; \
	fi

	if test '!' -d $(DESTDIR)$(cachedir); then \
		$(mkinstalldirs) $(DESTDIR)$(cachedir); \
		chmod 1755 $(DESTDIR)$(cachedir); \
		chown root:gdm $(DESTDIR)$(cachedir) || : ; \
	fi
