import pytest
import babelfish

"""
@pytest.fixture
def babelfish(request):
    test_babelfish = app.test_babelfish()

    def teardown():
        pass  #  need to be freed later

    request.addfinalizer(teardown)
    return test_babelfish
"""
TEST_FILES = [
    "sample.txt",
    "https://raw.githubusercontent.com/unfetter-discover/unfetter-insight/develop/sample.txt",
    "https://www.f-secure.com/documents/996508/1030745/blackenergy_whitepaper.pdf",
    "https://blogs.technet.microsoft.com/srd/2014/05/13/ms14-025-an-update-for-group-policy-preferences/"
    "http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory",
    "https://en.wikipedia.org/wiki/Command-line_interface",
    "https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html",
    "https://en.wikipedia.org/wiki/Code_signing",
    "https://securelist.com/operation-daybreak/75100/"
    "https://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf",
    "https://en.wikipedia.org/wiki/Server_Message_Block",
    "https://www.cylance.com/content/dam/cylance/pdfs/white_papers/RedirectToSMB.pdf"
    "https://osandamalith.com/2017/03/24/places-of-interest-in-stealing-netntlm-hashes/",
    "https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/",
    "https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf",
    "http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf",
    "https://www.slideshare.net/MatthewDunwoody1/no-easy-breach-derby-con-2016",
    "https://www.rsaconference.com/writable/presentations/file_upload/hta-f02-detecting-and-responding-to-advanced-threats-within-exchange-environments.pdf",
    "https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east",
    "https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html",
    "https://www.fireeye.com/services.html",
    "https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-finding-holes-operation-emmental.pdf",
    "https://en.wikipedia.org/wiki/Public-key_cryptography",
    "https://researchcenter.paloaltonetworks.com/2016/06/unit42-prince-of-persia-game-over/",
    "https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf",
    "https://www.crowdstrike.com/blog/mo-shells-mo-problems-deep-panda-web-shells/",
    "https://www.us-cert.gov/ncas/alerts/TA17-293A"
]

blackenergy_text = 'BLACKENERGY & QUEDAGH\nThe convergence of crimeware\nand APT attacks\nTLP: WHITE\nCONTENTS\nIntroduction\x082\nAttack overview\x08\n2\nInfection vectors\x08\n3\nTarget details\x08\n4\n2008 cyberattacks on Georgia?\x08\n4\nUkraine-related proxies\x08\n4\nTimeline\x086\nTechnical details\x08\n8\nUAC bypass during installation\x08\n8\nDriver signing policy bypass\x08\n8\nHijacking existing drivers\x08\n9\nDriver component\x08\n9\nMain DLL component\x08\n10\nBlackEnergy 3 \x08\n10\nInformation-stealing plugin\x08\n11\nNetwork traffic\x08\n12\nConclusions\x0813\nAppendix A | Samples\x08\n14\nBlackEnergy is a toolkit that has been used for years by various\ncriminal outfits. In the summer of 2014, we noted that certain\nsamples of BlackEnergy malware began targeting Ukranian\ngovernment organizations for information harvesting. These\nsamples were identified as being the work of one group,\nreferred to in this document as \xe2\x80\x9cQuedagh\xe2\x80\x9d, which has a history\nof targeting political organizations.\nThe Quedagh-related customizations to the BlackEnergy\nmalware include support for proxy servers and use of\ntechniques to bypass User Account Control and driver\nsigning features in 64-bit Windows systems. While monitoring\nBlackEnergy samples, we also uncovered a new variant used by\nthis group. We named this new variant BlackEnergy 3.\nThe use of BlackEnergy for a politically-oriented attack is an\nintriguing convergence of criminal activity and espionage. As\nthe kit is being used by multiple groups, it provides a greater\nmeasure of plausible deniability than is afforded by a custommade piece of code.\nF-SECURE LABS\nSECURITY RESPONSE\nMalware Analysis\nWhitepaper\n\x0cBLACKENERGY & QUEDAGH The convergence of crimeware and APT attacks\n2\nINTRODUCTION\nBlackEnergy is a popular crimeware (that is, malware\ndesigned to automate criminal activities) that is sold in the\nRussian cyber underground and dates back to as early as\n2007. Originally, it was designed as a toolkit for creating\nbotnets for use in conducting Distributed Denial of Service\n(DDoS) attacks. Over time, the malware has evolved to\nsupport different plugins, which are used to extend its\ncapabilities to provide necessary functions, depending on\nthe purpose of an attack.\nGiven the nature of its toolkit, BlackEnergy has\nunsurprisingly been used by different gangs for different\npurposes; some use it for sending spam, others for stealing\nbanking credentials. The most notorious use may be when\nit was used to conduct cyberattacks against Georgia during\nthe Russo-Georgian confrontation in 2008.\nIn the summer of 2014, BlackEnergy caught our attention\nwhen we noticed that samples of it were now tailored to\ntarget Ukrainian government institutions. Though it may\nbe unrelated, it is interesting to note that this change\nconveniently coincides with the on-going crisis in that\ncountry. Related or not, one thing is certain: the actor(s)\nusing these customized BlackEnergy malware are intent\non stealing information from the targets. The use of this\ncrimeware in what constitutes as an advance persistent\nthreat (APT) attack is interesting. In \xe2\x80\x98black operations\xe2\x80\x99\n(black ops), an important criteria is that the attack should\nnot be attributable - and what provides better plausible\ndeniability than crimeware known to be used by multiple\nparties?\nIn this paper we focus only on BlackEnergy samples\nknown to be used specifically by the actors we identify\nas Quedagh, who seem to have a particular interest in\npolitical targets. Special focus will be on the samples\nthat were used in targeted attacks against Ukrainian\ngovernment organizations earlier this year.\nATTACK OVERVIEW\nAt the time of writing, we have little information on how\nexactly victims are receiving the BlackEnergy malware\nbeing pushed by the Quedagh gang. An educated guess\nis that they are receiving the malware via targeted emails\ncontaining malicious attachments. Meanwhile, the\nfollowing infection and technical details are based on\nsamples gathered after searching through F-Secure Labs\xe2\x80\x99\ncollection of all BlackEnergy samples and identifying\nthose with Quedagh characteristics.\nThe BlackEnergy toolkit comes with a builder application\nwhich is used to generate the clients that the attacker(s)\nuse to infect victim machines. The toolkit also comes\nwith server-side scripts, which the attackers set up in\nthe command and control (C&C) server. The scripts also\nprovide an interface where an attacker can control his\nbots. The simplicity and convenience provided by the\ntoolkit means that anyone who has access to the kit can\nbuild his own botnet without any skills required.\nFigure 1: BlackEnergy Builder from 2007\n\x0cThe convergence of crimeware and APT attacks BLACKENERGY & QUEDAGH\n3\nThe original BlackEnergy toolkit first emerged in 2007 and\nis referred to in this paper as BlackEnergy 1. A later variant\nof the toolkit (BlackEnergy 2) was released in 2010. We also\nencountered a previously unseen variant, which had been\nrewritten and uses a different format for its configuration.\nIt also no longer uses a driver component. We dubbed this\nnew variant BlackEnergy 3.\nINFECTION VECTORS\nMost of the recent BlackEnergy installers collected are\nnamed msiexec.exe. We believe they are either dropped\nby another executable that uses social engineering tricks\nto mislead the user into executing the installer, or by\ndocuments containing exploits that silently perform the\ninstallation.\nWe found at least 2 trojanized legitimate applications that\nexecute the installer (in addition to their legitimate tasks).\nTrojanization is an effective infection method, as most\nusers have no way of observing that a malicious component\nis being installed in tandem with a legitimate program.\nSome earlier installer variants, then named regedt32.\nexe, were distributed by documents exploiting software\nvulnerabilities, one of which was CVE-2010-3333. These\ndocuments drop and execute the installer, then open a\ndecoy document. It is reasonable to assume that a similar\napproach has been used to deliver the more recent\ninstaller variants.\nThe installer filename of BlackEnergy 3 is still msiexec.exe.\nHowever, it is delivered and executed by a dropper which\nopens a decoy document in the foreground. We also\nencountered a standalone, non-persistent sample that\npretends to be Adobe Flash Player Installer. It does not use\nany decoy document or application and does not run after\nreboot.\nThe overview below summarizes the various infection\nvectors used by the Quedagh gang to deliver BlackEnergy\ncrimeware to the designated targets.\nOVERVIEW OF INFECTION VECTORS USED AGAINST UKRAINIAN TARGETS\nmsiexec.exe\nINSTALLER\nAPP\nTrojanized\napp\nAPP\nClean\napp\nmsiexec.exe\nINSTALLER\nExploit\ndocument\nPERSISTENT\ncomponent\nDecoy\ndocument\nmsiexec.exe\nINSTALLER\nDropper\nmalware\nDecoy\ndocument\nNON-PERSISTENT\ncomponent\nFake\ninstaller\nPERSISTENT\ncomponent\nPERSISTENT\ncomponent\n\x0cBLACKENERGY & QUEDAGH The convergence of crimeware and APT attacks\n4\nTARGET DETAILS\nFrom the very earliest variants we were able to attribute\nto Quedagh, we have noticed that their targets have been\npolitical in nature. Apart from other indicators, we can\ndeduce the nature of the target based on the content of\nsocial engineering tactics used to distribute the installers.\nFor example, one decoy dropped from a sample dating to\n2012 (image 2) seems to be targeting European audiences\nand discusses a political/economic situation. Strings found\nin another sample from 2012 (image 3) again indicate\na political motivation behind the attack. Most decoys\nused content taken from news sites; we noted one decoy\ndropped by an exploit document was created using the\nRussian version of Office (image 4).\nImage 2:\nDecoy document circa 2012\nThe latest variant of the dropper pretends to be a\ndocument file with a Ukrainian filename (image 5).\nThe choice of language for the filename again may tie\nin or reference the current political crisis in that country.\nThe filename itself means \xe2\x80\x98password list\xe2\x80\x99 in English.\n2008 CYBERATTACKS ON GEORGIA?\nDuring our investigation, we found interesting details\nthat lead us to suspect that Quedagh might have been\ninvolved in the cyberattacks launched against Georgia\nduring the 2008 Russo-Georgian confrontation. While the\ndetails identified are suggestive, they are not conclusive;\nthey do however seem consistent with the group\xe2\x80\x99s\ninvolvement in subsequent targeted attacks.\nUKRAINE-RELATED PROXIES\nWhile examining the samples collected during our\nBlackEnergy monitoring, we noticed that samples from\nthis year had been updated to support the use of proxy\nservers while connecting to their C&C servers. This\ncontrasts with earlier BlackEnergy 2 variants, which do\nnot support proxy servers. In some network setups, a\nproxy server is needed to allow internal users to access\nthe Internet [1]. BlackEnergy\xc2\xb9s use of a proxy server may\nindicate that the gang has prior knowledge of the target\norganization\xe2\x80\x99s internal setup to note of this requirement.\nFor example, in one sample the configuration uses\nthe proxy server associated with the Ukrainian Railway\n(image 6). The configuration from another sample\nalso shows it using an internal proxy under the giknpc\ndomain (image 7). The domain giknpc.com.ua in turn\nhosts 3 domains (image 8), one of which is for the city\nof Dnipropetrovsk (image 9), the fourth-largest city in\nUkraine, located in the southeast. Based on the set proxy\nservers for the different samples, we concluded that the\ngang is targeting Ukrainian government organizations.\nImage 3:\nStrings from a sample circa 2012\n\x0cThe convergence of crimeware and APT attacks BLACKENERGY & QUEDAGH\n5\nImage 4:\nDecoy document created using a Russian version of Office\nImage 5:\n2014 dropper sample disguised as a document. The filename means password list\nImage 6:\nConfiguration using Ukrainian Railway\xe2\x80\x99s proxy\nImage 7:\nConfiguration using internal proxy under giknpc domain\nImage 8:\nDomains hosted on giknpc.com\nImage 9:\nDnipropetrovsk domain\n\x0cBLACKENERGY & QUEDAGH The convergence of crimeware and APT attacks\n6\nTIMELINE\nAlthough they may have started much earlier, the earliest\nBlackEnergy sample we could attribute to the Quedagh\ngang is from December 14, 2010.\nInitially, the group seemed to prefer to use the filename of\nthe Windows registry editor (regedt32.exe), presumably\nbecause the installer needs administrator rights to install\nits driver component and therefore would try to request\nfor the highest available rights (image 10), if possible. As\nthis triggers a notification message visible to the user, said\nuser is more likely to grant permission if it appears to be\nthe registry editor that is requesting for permission, since\nit is normal to run it with administrator rights. Experienced\nusers though are less likely to be taken in, thereby\ndecreasing the likelihood of a successful infection.\nImage 10:\nInstaller requesting highest available rights\nStarting April 2013, modified installers appeared showing\nthat the Quedagh group found a way to bypass the default\nUser Account Control (UAC) settings. With this change,\nthe user\xe2\x80\x99s permission is no longer need (image 11). At this\npoint, the gang also began to use the Windows installer\nprogram filename msiexec.exe.\n64-bit support\nWithin a month of Windows 8.1\xe2\x80\x99s release, the gang\nhad quickly added support for 64-bit systems, possibly\nanticipating that more of their target systems will be\nmigrated to 64-bit systems. They also employ a neat\ntrick to bypass the driver signing requirement on 64bit Windows systems. As a side note, this latest finding\nupdates and supercedes previously published research\nrelated to BlackEnergy\xe2\x80\x99s driver signing behavior [2].\nHowever, this trick doesn\xe2\x80\x99t work on Windows 8 and\nlater systems. The driver also crashes occassionally. This\ncould be the reason for the stand-alone non-persistent\nBlackEnergy variant.\nBlackEnergy 3\nWe identified the new BlackEnergy 3 variant first by the\nchange in its configuration, which differed from those\nof its two predecessors, 1 and 2 (images 12 to 14). It also\nno longer uses a driver component [3]. Further technical\ndetails are documented on page 10 to 11.\nImage 11:\nInstaller execution privilege level amended\n\x0cTIMELINE OF BLACKENERGY & QUEDAGH HISTORY\nBLACKENERGY Development\nBlackEnergy\n1\nMay 12\nBlackEnergy\n2\nQuedagh APT campaign\nBlackEnergy\n3\nApr 9\nDec 14\nCYBERATTACKS\nAGAINST\nGEORGIA\n2008\n2009\nSome time\nafter Dec 25\n64-bit\nNew UACTargets\nbypassing support for Ukrainian\nBlackEnergy entities\ninstaller\n(msiexec.exe) 2 driver\nFirst installer\n(regedt32.exe)\n2007\nNov 14\nPOLITICAL\nCRISIS IN\nUKAINE\n2010\n2011\n2012\n2013\nImage 12: BlackEnergy 1 configuration\nImage 13: BlackEnergy 2 (aka BotnetKernel or bkernel [4] ) configuration\nImage 14: BlackEnergy 3 configuration\n2014\n\x0cBLACKENERGY & QUEDAGH The convergence of crimeware and APT attacks\n8\nTECHNICAL DETAILS\nUAC BYPASS DURING INSTALLATION\nDRIVER SIGNING POLICY BYPASS\nThe malware will only attempt to infect a system if the\ncurrent user is a member of the local administrator group.\nIf not, it will re-launch itself as Administrator on Vista.\nThis in effect will trigger a UAC prompt. On Windows 7\nand later however, the malware will attempt to bypass the\ndefault UAC settings. It exploits a backward-compatibility\nfeature found in newer versions of Windows. BlackEnergy\ninstallers include a Shim Database, or a \xe2\x80\x9cfix\xe2\x80\x9d, instructing\nSndVol.exe to execute cmd.exe (image 15, below) instead\nin order to resolve the incompatibility.\nThe role of the installer is to set up the malware\xe2\x80\x99s\npersistent component, which is the driver component.\nOn 64-bit Windows systems, Microsoft has enforced a\npolicy that requires all drivers to be signed as a security\nprecaution. Signing provides a way to identify a driver to\nits author, effectively reducing the number of malware\ndevelopers willing to take the risk. To allow developers to\ntest their drivers during development, Microsoft provides\na TESTSIGNING boot configuration option; while in this\nmode, a watermark is displayed on the screen to make it\nobvious to users and to prevent malware from exploiting\nthis option.\nSndVol.exe is one of the Windows executables that will\nbe automatically elevated upon execution because it\nis thought to be safe. What harm can a volume control\ncause? With the malicious \xe2\x80\x9cfix\xe2\x80\x9d installed however,\nexecuting SndVol.exe will execute the not-so-safe file\ncmd.exe instead, which can then be used to install the\nmalware while in an elevated state.\nBlackEnergy enables the TESTSIGNING option to load its\ndriver component; to hide this change from the user, the\nmalware removes the watermark by removing the relevant\nstrings in the user32.dll.mui of the system. In Windows\n8 and up however, the strings are no longer stored in\nuser32.dll.mui, so the trick will not work. This may be one\nof the reasons for the existence of a standalone nonpersistent BlackEnergy variant. The malware does not\ninfect 64-bit Windows systems that are older than Vista.\nImage 15: Malicious fix to redirect SndVol.exe to cmd.exe. Inset: Test Mode watermark\n\x0cThe convergence of crimeware and APT attacks BLACKENERGY & QUEDAGH\n9\nDIAGRAM 1: INSTALLATION FLOW\nDIAGRAM 2: ROLE OF DRIVER COMPONENT\nNeed rights?\nINSTALLER\nTemporary\ncomponent\nRun as\nadministrator\nBypass UAC\nInstalls\nPersistent\ncomponent\nDRIVER\nInjects\nAdditional steps\non 64-bit systems\nsvchost.exe\nEnable\nTESTSIGNING\nMAIN DLL\nRemove Test\nMode watermark\nTABLE 1: IOCTL BUFFER COMMAND CODES\nLocate inactive\ndrivers\nReplace with\ndriver component\nCode\nFunction\n6\nLoads a driver into memory\n9\nDoes not do anything; just returns true.\nPreviously contained an uninstall routine.\n10\nReturns the registry path and driver file path\nHIJACKING EXISTING DRIVERS\nDRIVER COMPONENT\nThe installer will try to locate an existing driver service\nthat is inactive. The service found will usually be a\nlegitimate one that is disabled because it is no longer\nused or because it is set to start only on demand. The\ninstaller will drop the driver component using the\ncorresponding path of the service. It will overwrite the\nexisting driver if necessary. The hijacked service is then\nset to start automatically. This is how the malware is able\nto survive after a reboot. By doing this, the gang may be\nhoping that their malicious driver will be overlooked by\nadministrators or investigators who are so used to seeing\nthose legitimate services.\nThe only component that will remain permanently on the\ninfected system will be the driver component. The driver\ncomponent used by the gang is a stripped down version\nof the BlackEnergy 2 driver.\nThe sole purpose of this driver component is to inject\nthe main DLL component into svchost.exe. Interestingly,\nit does not contain the rootkit functionalities for hiding\nprocesses, files and registry objects that is found in the\nusual BlackEnergy 2 drivers. The gang may have opted for\na \xe2\x80\x98hide in plain sight\xe2\x80\x99 approach to evade detections from\nrootkit scanners, such as GMER and RootkitRevealer, that\nchecks for system anomalies.\nThe driver component provides a IOCTL interface to\ncommunicate with the main DLL component. Table 1\n(above) summarizes the command codes that can be\npassed to the IOCTL buffer. The 32-bit version contains\nadditional, incomplete routines for hiding processes via\ndirect kernel object manipulation (DKOM) and managing\nBlackEnergy 2 rootkit rules in memory [2].\n\x0cBLACKENERGY & QUEDAGH The convergence of crimeware and APT attacks\n10\nTABLE 2: TYPICAL BLACKENERGY DRIVER COMPONENT\nVERSUS QUEDAGH\xe2\x80\x99S CUSTOM COMPONENT\nTypical BlackEnergy 2\nQuedagh BlackEnergy 2\nLaunch Point\nCreates a new service based on either\na hardcoded or randomly generated\nname (depending on the installer)\nHijacks an existing legitimate service\nRole\nHides processes, files and registry\nobjects; Inject main DLL to svchost.exe\nInjects main DLL to svchost.exe\nVersions\n32-bit driver component that contains\ncomplete routines in its IOCTL\ninterface\n32-bit driver component with a lot of remnant routines in\nits IOCTL interface, only a few of which make sense.\nAfter Nov 11, 2013, the 64-bit driver component is available\nand provides limited functionalities in IOCTL interface (only\nthose equivalent working routines found in the 32-bit versions)\nTABLE 3: COMMANDS SUPPORTED BY VARIANTS\nTARGETED AT UKRAINIAN ENTITIES\nCommand\nDescription\nrexec\nDownload and execute a binary\nlexec\nExecute a shell command\ndie\nUninstall\ngetpl\nLoad a plugin\nturnoff\nQuit (will start again after reboot)\nchprt\nAdd / remove / set active command and control server\nBlackEnergy 2 was very well documented by Dell\nSecureWorks [5] in 2010. Table 2 (above) summarizes\nthe differences between the driver component used by\nQuedagh compared to the typical BlackEnergy 2.\nMAIN DLL COMPONENT\nThe core functionality of BlackEnergy 2 is found in the\nmain DLL component. This component is embedded inside\nthe driver component and is not found in the file system;\nthis is to reduce the infection footprint on the system.\nThe main DLL provides a robust framework for attackers\nto maintain a botnet that is not tied to any specific\nfunctionality. The malware is designed to be used by\nloading customized plugins depending on the purpose\nof the botmaster. It is mainly a framework for plugins\nto communicate with a central command and control.\nOtherwise, the main DLL only provides a minimal set of\ncommands. Table 3 (above) summarizes the commands\nsupported by the variants used in the attack against\nUkrainian government organizations.\nIn BlackEnergy 2, the main DLL component communicates\nwith its plugins via a defined set of API calls. It exports\na number of function calls, which can be used by the\nplugins. On the other hand, plugins are required to export\n2 functions to work. We highly recommend the research\nof Dell SecureWorks for those looking for more details\nregarding the BlackEnergy 2 plugin framework.\nBLACKENERGY 3\nIn contrast to previous variants, BlackEnergy 3 uses a\nsimpler installer component. It does not have a driver\ncomponent and the installer drops the main DLL\ncomponent directly to the local application data (nonroaming) folder. The installer then creates a LNK file in the\nstartup folder, using a filename generated based on the\nvolume serial number as a launch point. The LNK file is a\nshortcut to execute the main DLL using rundll32.exe.\n\x0cThe convergence of crimeware and APT attacks BLACKENERGY & QUEDAGH\n11\nTABLE 4: X509_ASN FIELDS & EQUIVALENT\nBLACKENERGY 2 XML NODE\nID\nBlackEnergy 2\nNode\nDescription\n1\nservers\nThe command and control servers\n2\nplugins\nPlugins to be loaded\n3\ncmds\nCommands to be executed\n4\nbuild id\nBuild ID\n5\nsleepfreq\nPhone home interval\nThis variant uses a new configuration format. The\nconfiguration data is a series of X509_ASN encoded values\nand are accessed by an ID number. Table 4 summarizes\nthe fields and their equivalent BlackEnergy 2 XML node,\nwhile table 5 lists the completely new set of commands\nused in this latest variant.\nBlackEnergy 3 also uses a different method of\ncommunication with its plugins, as it now communicates\nvia RPC over the named-pipe protocol (ncacn_np).\nINFORMATION-STEALING PLUGIN\nSince the main DLL component offers little clue as to what\nthe malware was used for, we need to look at the plugin to\ndetermine the objective of the gang.\nOne particular plugin that was used in the campaign was\ncalled \xe2\x80\x9csi\xe2\x80\x9d, perhaps to mean \xe2\x80\x98steal information\xe2\x80\x99. The latest\nsample we found will attempt to gather the following\ninformation and send them to the C&C server:\n\xe2\x80\xa2 System configuration information (gathered via\nsysteminfo.exe)\n\xe2\x80\xa2 Operating system version\n\xe2\x80\xa2 Privileges\n\xe2\x80\xa2 Current time\n\xe2\x80\xa2 Up time\n\xe2\x80\xa2 Idle Time\n\xe2\x80\xa2 Proxy\n\xe2\x80\xa2 Installed apps (gathered from uninstall program\nregistry)\n\xe2\x80\xa2 Process list (gathered via tasklist.exe)\n\xe2\x80\xa2 IP configurations (gathered via ipconfig.exe)\n\xe2\x80\xa2 Network connections (gathered via netstat.exe)\n\xe2\x80\xa2 Routing tables (gathered via route.exe)\n\xe2\x80\xa2 Traceroute and Ping information to Google\n(gathered via tracert.exe and ping.exe)\n\xe2\x80\xa2 Registered mail, browser, and instant messaging\nclients (gathered via client registry)\nTABLE 5: BLACKENERGY 3\nCOMMANDS\nCommand\nDescription\ndelete\nUninstall\nldplg\nLoad a plugin\nunlplg\nUnload a plugin\nupdate\nUpdate main DLL\ndexec\nDownload and execute an executable\nexec\nDownload and execute a binary\nupdcfg\nUpdate the configuration data\n\xe2\x80\xa2 Account and password information from The\nBat! email client (gathered from account.cfn and\naccount.cfg)\n\xe2\x80\xa2 Stored username and passwords in Mozilla\npassword manager of the following applications\n(gathered from signons*.txt and signons.sqlite)\n\xe2\x80\xa2 Thunderbird\n\xe2\x80\xa2 Firefox\n\xe2\x80\xa2 SeaMonkey\n\xe2\x80\xa2 IceDragon\n\xe2\x80\xa2 Stored username and passwords in Google\nChrome password manager of the following\napplications (gathered from \xe2\x80\x9cLogin Data\xe2\x80\x9d)\n\xe2\x80\xa2 Google Chrome\n\xe2\x80\xa2 Chromium\n\xe2\x80\xa2 Comodo Dragon\n\xe2\x80\xa2 Xpom\n\xe2\x80\xa2 Nichrome\n\xe2\x80\xa2 QIP Surf\n\xe2\x80\xa2 Torch\n\xe2\x80\xa2 YandexBrowser\n\xe2\x80\xa2 Opera\n\xe2\x80\xa2 Sleipnir\n\xe2\x80\xa2 Account and password information from Outlook\nand Outlook Express\n\xe2\x80\xa2 Internet Explorer version and stored username\nand passwords\n\xe2\x80\xa2 Stored username and passwords in Windows\nCredential Store\n\xe2\x80\xa2 Live\n\xe2\x80\xa2 Remote Desktop\n\xe2\x80\xa2 Other generic credentials (Microsoft_\nWinInet_*)\nThe nature of the information being gathered seems to\nbe generic rather than targeted. This may be because the\nmalware has roots from crimeware. The information is still\nuseful however as such data makes it easier for the gang\nto plan any further attacks on the same targets.\n\x0cBLACKENERGY & QUEDAGH The convergence of crimeware and APT attacks\n12\nDIAGRAM 3: CONFIGURATION DATA HANDLING\n1\nHTTP POST\n2\nMAIN DLL\n1\nC&C\nSERVER\nConfig\nConfig\n3\nMain DLL process configuration data embedded\nin its body; will only process fields related to C&C\ncommunication. BlackEnergy 2 configuration may\nalso contain initial commands to execute.\n2\nMain DLL reports to C&C.\n3\nMain DLL processes the configuration data\nreturned by the C&C. This time, it processes\nfields related to plugins and commands.\nTABLE 6: MAIN DLL\xe2\x80\x99S ADDITIONAL COMMANDS\nDURING DOWNLOAD OF ADDITIONAL FILES\nHTTP POST Field\nDescription of Values\ngetp\nThe plugin name to be downloaded\nplv\nSome variants specify the version of the plugin to be downloaded\ngetpd\nThe binary name to be downloaded\nNETWORK TRAFFIC\nBlackEnergy communicates with its C&C server via HTTP\nPOST requests. For the BlackEnergy 2 samples used by the\ngang, the request contains the following fields:\nid=[bot_id]&bid=[base64_encoded_build_\nid]&dv=[x]&mv=[y]&dpv=[z]\nWhere:\n\xe2\x80\xa2 bot_id is equivalent to the infected host name\nand the volume serial number following the\nformat x[host_name]_[serial_no] (e.g. xJOEPC_484DA98A)\n\xe2\x80\xa2 build_id is the string found in the build_id field in\nthe sample\xe2\x80\x99s configuration data\n\xe2\x80\xa2 x, y, z are hardcoded values which varies among\nsamples\nThe fields are almost the same for BlackEnergy 3 samples:\nid=[bot_id_sha1]&bid=[base64_encoded_build_\nid]&nm=[x]&cn=[y]&num=[z]\nThe only major difference is that the id field contain just\nthe hash instead of the actual string. The actual bot_id\nstring in which the id hash is derived is also a bit different;\nit now uses the format [domain_sid]_[host_name]_\n[serial_no].\nThe response of the command and control server will\nbe encrypted using the id field in the POST request as\nthe key. After the response is decrypted, it will be in the\nform of the corresponding configuration data of the\nBlackEnergy sample; for example, BlackEnergy 2 samples\nexpect the decrypted response to be a XML document,\nwhile BlackEnergy 3 samples expect the decrypted\nresponse to be a series X509_ASN encoded values.\nThe decrypted response, which is equivalent to another\nconfiguration data, will be processed similar to the initial\nconfiguration data embedded in the main DLL; the only\ndifferences are the data fields that are processed. This\ncycle is illustrated in diagram 3 (above).\nThe main DLL also uses the fields listed in table 6 (above)\nwhen it needs to download additional files.\n\x0cThe convergence of crimeware and APT attacks BLACKENERGY & QUEDAGH\n13\nCONCLUSIONS\nBlackEnergy is a toolkit that has been used for years\nby various criminal outfits. In the summer of 2014, we\nnoted that certain samples of BlackEnergy malware\nbegan targeting Ukranian government organizations for\ninformation harvesting. These samples were identified as\nbeing the work of one group, referred to in this document\nas \xe2\x80\x9cQuedagh\xe2\x80\x9d, which has a history of targeting political\norganizations. Though inconclusive, suggestive details\nindicate that BlackEnergy malware, possibly also from this\ngang, may also have been used in the Russo-Georgian\nconfrontation in 2008.\nThe Quedagh-customizations to the BlackEnergy malware\ninclude support for proxy servers (which, in the samples\nexamined are associated with Ukrainian entities) and\nuse of techniques to bypass User Account Control and\ndriver signing features in 64-bit Windows systems. While\nmonitoring BlackEnergy samples, we also encountered a\nnew variant, which we dub BlackEnergy 3, with a modified\nconfiguration, no driver component and a different\ninstallation procedure.\nThe use of BlackEnergy for a politically-oriented attack\nis an intriguing convergence of criminal activity and\nespionage. As the kit is being used by multiple groups, it\nprovides a greater measure of plausible deniability than is\nafforded by a custom-made piece of code.\n.REFERENCES\n1. Wikipedia; Proxy server; http://en.wikipedia.org/wiki/Proxy_server#Cross-domain_resources\n2. Broderick Aquilino; F-Secure Weblog; BlackEnergy Rootkit, Sort Of; 13 June 2014;\nhttp://www.f-secure.com/weblog/archives/00002715.html\n3. Broderick Aquilino; F-Secure Weblog; Beware BlackEnergy If Involved In Europe/Ukraine Diplomacy; 30 June 2014;\nhttp://www.f-secure.com/weblog/archives/00002721.html\n4. Kafeine; Malware don\xe2\x80\x99t need Coffee; BotnetKernel (MS:Win32/Phdet.S) an evolution of BlackEnergy ; 21 June 2014;\nhttp://malware.dontneedcoffee.com/2014/06/botnetkernel.html\n5. Joe Stewart; DELL SecureWorks; BlackEnergy Version 2 Analysis; 3 March 2010;\nhttp://www.secureworks.com/cyber-threat-intelligence/threats/blackenergy2/\n\x0cBLACKENERGY & QUEDAGH The convergence of crimeware and APT attacks\n14\nAPPENDIX A | SAMPLES\nSHA1\nDescription\n26b9816b3f9e2f350cc92ef4c30a097c6fec7798\nMain reference for related BlackEnergy 2 32-bit driver and main\nDLL component analysis\nbf9937489cb268f974d3527e877575b4fbb07cb0\nMain reference for related BlackEnergy 2 64-bit driver (signed\non 2013-12-25) and installer analysis. Basis for the start of the\nUkrainian target.\n78636f7bbd52ea80d79b4e2a7882403092bbb02d\nMain reference for related BlackEnergy 3 analysis\nbf9172e87e9264d1cddfc36cbaa74402bb405708\nMain reference for related si plugin analysis\n441cfbaba1dfd58ce03792ef74d183529e8e0104\nStand-alone non-persistent BlackEnergy 2 sample\nf7d4aa90b76646f4a011585eb43b9d13c60f48eb\nTrojanized Juniper installer containing related BlackEnergy 2\n8ccd2962bce8985d0794daed6e0bf73e5557cfe8\nTrojanized Adobe Bootstrapper containing related BlackEnergy\n2. This means that it is highly probable that there is a trojanized\nAdobe package out there.\nd496f99f7e07d5cbbd177a9d43febe8fb87ebc3b\nRelated RTF document containing exploit\ncc71aa8f919911676fb5d775c81afc682e6e3dd3\nRelated BlackEnergy 2 binary containing strings that are\npolitical in nature\nabab02d663872bcdbe2e008441fcd7157c0eb52d\nOldest (compiled on 2010-12-14) related BlackEnergy 2 installer\nthat was found\ne5c8c10b10ee288512d3a7c79ae1249b57857d23\nOldest (compiled on 2013-04-09) related BlackEnergy 2\ninstaller that bypass UAC that was found\n8743c8994cc1e8219697394b5cb494efa7dad796\nOldest (signed on 2013-11-14) related BlackEnergy 2 64-bit\ndriver that was found\n285b3252a878d1c633ea988153bbc23c148dd630\nOldest (compiled on 2014-05-12) related BlackEnergy 3 dropper\nthat was found\n\x0cThe convergence of crimeware and APT attacks BLACKENERGY & QUEDAGH\n15\nPAGE INTENTIONALLY LEFT BLANK\n\x0cSWITCH\nON\nFREEDOM\nF-Secure is an online security and privacy company from Finland. We\nF-Secure\nis anof\nonline\nsecurity\nFinland.\noffer millions\npeople\naroundand\nthe privacy\nglobe thecompany\npower tofrom\nsurf invisibly\nWe offerand\nmillions\nof people\naround\nglobe\nthethreats.\npower to surf\nstore and\nshare stuff,\nsafethe\nfrom\nonline\ninvisibly and store and share stuff, safe from online threats.\nWe are here to fight for digital freedom.\nWe are here to fight for digital freedom.\nJoin the movement and switch on freedom.\nJoin the movement and switch on freedom.\nFounded in 1988, F-Secure is listed on NASDAQ OMX Helsinki Ltd.\nFounded in 1988, F-Secure is listed on NASDAQ OMX Helsinki Ltd.'

"""
@pytest.mark.parametrize("test_input", TEST_FILES)
def test_classify_report(test_input):
    test_list = babelfish.classify_report(test_input)
    assert len(test_list) != 0
"""
@pytest.mark.parametrize("test_input", TEST_FILES)
def test_tag_report(test_input):
    plot, text = babelfish.plot_report(test_input)
    x = babelfish.tag_report(text, test_input)
    assert len(x) != 0
"""
def test_tag_report_one():
    plot, text = babelfish.plot_report("blackenergy_whitepaper.pdf")
    assert text == blackenergy_text
    x = babelfish.tag_report(text, "blackenergy_whitepaper.pdf")
    
def test_tag_report_two():
    plot, text = babelfish.plot_report("https://www.f-secure.com/documents/996508/1030745/blackenergy_whitepaper.pdf")
    assert text == blackenergy_text
    x = babelfish.tag_report(text, "https://www.f-secure.com/documents/996508/1030745/blackenergy_whitepaper.pdf")
"""