;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;--------------------------------
;General

  ;Name and file
  Name "Electrum-NMC"
  OutFile "dist/electrum-NMC-setup.exe"

  ;Default installation folder
  InstallDir "$PROGRAMFILES\Electrum-NMC"

  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\Electrum-NMC" ""

  ;Request application privileges for Windows Vista
  RequestExecutionLevel admin

;--------------------------------
;Variables

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  ;!insertmacro MUI_PAGE_LICENSE "tmp/LICENCE"
  ;!insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY

  ;Start Menu Folder Page Configuration
  !define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU"
  !define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\Electrum-NMC"
  !define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"

  ;!insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder

  !insertmacro MUI_PAGE_INSTFILES

  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES

;--------------------------------
;Languages

  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Section

  SetOutPath "$INSTDIR"

  ;ADD YOUR OWN FILES HERE...
  file /r dist\electrum-NMC\*.*

  ;Store installation folder
  WriteRegStr HKCU "Software\Electrum-NMC" "" $INSTDIR

  ;Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"


  CreateShortCut "$DESKTOP\Electrum-NMC.lnk" "$INSTDIR\electrum-NMC.exe" ""

  ;create start-menu items
  CreateDirectory "$SMPROGRAMS\Electrum-NMC"
  CreateShortCut "$SMPROGRAMS\Electrum-NMC\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\Electrum-NMC\Electrum-NMC.lnk" "$INSTDIR\Electrum-NMC.exe" "" "$INSTDIR\Electrum-NMC.exe" 0

SectionEnd

;--------------------------------
;Descriptions

  ;Assign language strings to sections
  ;!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  ;  !insertmacro MUI_DESCRIPTION_TEXT ${SecDummy} $(DESC_SecDummy)
  ;!insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;Uninstaller Section

Section "Uninstall"

  ;ADD YOUR OWN FILES HERE...
  RMDir /r "$INSTDIR\*.*"

  RMDir "$INSTDIR"

  Delete "$DESKTOP\Electrum-NMC.lnk"
  Delete "$SMPROGRAMS\Electrum-NMC\*.*"
  RmDir  "$SMPROGRAMS\Electrum-NMC"

  DeleteRegKey /ifempty HKCU "Software\Electrum-NMC"

SectionEnd
