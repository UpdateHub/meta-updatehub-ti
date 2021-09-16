FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append:updatehub-ti = "\
    file://fw_env.config \
    file://updatehub.cfg \
"


