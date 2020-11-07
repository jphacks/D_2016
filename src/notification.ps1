Function Toast {
    #AppID調べる:Get-StartApps
    $AppId = "{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe"

    #ロード済み一覧:[System.AppDomain]::CurrentDomain.GetAssemblies() | % { $_.GetName().Name }
    #WinRTAPIを呼び出す:[-Class-,-Namespace-,ContentType=WindowsRuntime]
    $null = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
    $null = [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]
    
    #XmlDocumentクラスをインスタンス化
    $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
    #LoadXmlメソッドを呼び出し、変数templateをWinRT型のxmlとして読み込む
    $xml.LoadXml($template)

    #ToastNotificationクラスのCreateToastNotifierメソッドを呼び出し、変数xmlをトースト
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($AppId).Show($xml)
}


#トーストテンプレート
$src_name = "mirai.gif"

Write-Host = $Args[0] 
Write-Host = $Args[1] 

$src_name = $Args[1]
$txt = $Args[0]

$dir_path = Join-Path $PSScriptRoot "media" 
$img_path = Join-Path $dir_path $src_name
$icon_path = Join-Path $dir_path "komati.ico"
echo $icon_path

$time = "long"
$template = @"
<toast duration="$time">
    <visual>
        <binding template="ToastGeneric">
            <text> $txt </text>
            <image placement="appLogoOverride" hint-crop="circle" src="$icon_path"/>
            <image placement="hero" src="$img_path"/>
        </binding>
    </visual>
    <actions>

            <action
                content="Thank you"
                arguments="action=remindlater&amp;contentId=351"
                activationType="background"/>

    </actions>
</toast>
"@
            
#<audio silent="false" src="ms-appx:///Assets/NewMessage.mp3"/>
Toast
exit