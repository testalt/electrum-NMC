#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('util', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = util.usr_share_dir()
if not os.access(usr_share, os.W_OK):
    try:
        os.mkdir(usr_share)
    except:
        sys.exit("Error: cannot write to %s.\nIf you do not have root permissions, you may install Electrum in a virtualenv.\nAlso, please note that you can run Electrum without installing it on your system."%usr_share)

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-NMC.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-NMC.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = os.path.join(usr_share, "electrum-NMC")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]

for lang in os.listdir('data/wordlist'):
    data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))


setup(
    name="Electrum-NMC",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'pyasn1',
        'pyasn1-modules',
        'qrcode',
        'SocksiPy-branch',
        'tlslite'
    ],
    package_dir={
        'electrum-NMC': 'lib',
        'electrum_NMC_gui': 'gui',
        'electrum_NMC_plugins': 'plugins',
    },
    scripts=['electrum-NMC'],
    data_files=data_files,
    py_modules=[
        'electrum_NMC.account',
        'electrum_NMC.bitcoin',
        'electrum_NMC.blockchain',
        'electrum_NMC.bmp',
        'electrum_NMC.commands',
        'electrum_NMC.daemon',
        'electrum_NMC.i18n',
        'electrum_NMC.interface',
        'electrum_NMC.mnemonic',
        'electrum_NMC.msqr',
        'electrum_NMC.network',
        'electrum_NMC.network_proxy',
        'electrum_NMC.old_mnemonic',
        'electrum_NMC.paymentrequest',
        'electrum_NMC.paymentrequest_pb2',
        'electrum_NMC.plugins',
        'electrum_NMC.qrscanner',
        'electrum_NMC.simple_config',
        'electrum_NMC.synchronizer',
        'electrum_NMC.transaction',
        'electrum_NMC.util',
        'electrum_NMC.verifier'
        'electrum_NMC.version',
        'electrum_NMC.wallet',
        'electrum_NMC.x509',
        'electrum_NMC_gui.gtk',
        'electrum_NMC_gui.qt.__init__',
        'electrum_NMC_gui.qt.amountedit',
        'electrum_NMC_gui.qt.console',
        'electrum_NMC_gui.qt.history_widget',
        'electrum_NMC_gui.qt.icons_rc',
        'electrum_NMC_gui.qt.installwizard',
        'electrum_NMC_gui.qt.lite_window',
        'electrum_NMC_gui.qt.main_window',
        'electrum_NMC_gui.qt.network_dialog',
        'electrum_NMC_gui.qt.password_dialog',
        'electrum_NMC_gui.qt.paytoedit',
        'electrum_NMC_gui.qt.qrcodewidget',
        'electrum_NMC_gui.qt.qrtextedit',
        'electrum_NMC_gui.qt.receiving_widget',
        'electrum_NMC_gui.qt.seed_dialog',
        'electrum_NMC_gui.qt.transaction_dialog',
        'electrum_NMC_gui.qt.util',
        'electrum_NMC_gui.qt.version_getter',
        'electrum_NMC_gui.stdio',
        'electrum_NMC_gui.text',
        'electrum_NMC_plugins.btchipwallet',
        'electrum_NMC_plugins.coinbase_buyback',
        'electrum_NMC_plugins.cosigner_pool',
        'electrum_NMC_plugins.exchange_rate',
        'electrum_NMC_plugins.greenaddress_instant',
        'electrum_NMC_plugins.labels',
        'electrum_NMC_plugins.trezor',
        'electrum_NMC_plugins.virtualkeyboard',
        'electrum_NMC_plugins.plot',

    ],
    description="Lightweight Namecoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="https://namecoin.electrum-alt.org",
    long_description="""Lightweight Namecoin Wallet"""
)
