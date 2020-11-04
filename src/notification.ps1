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
$src_name = "media\mirai.gif"
$txt = "こんにちは"

$img_path = Join-Path $PSScriptRoot $src_name
$template = @"
<toast duration="1">
    <visual>
        <binding template="ToastGeneric">
            <text> $txt </text>
            <image placement="hero" src="$img_path"/>
        </binding>
    </visual>
    <audio silent="false" src="ms-winsoundevent:Notification.Default" />
</toast>
"@

Toast
exit