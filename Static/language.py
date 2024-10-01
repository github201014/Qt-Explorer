from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
def zh_CN(web: QWebEngineView):
    pass
    web.pageAction(QWebEnginePage.WebAction.Back).setText("返回")
    web.pageAction(QWebEnginePage.WebAction.Forward).setText("前进")
    web.pageAction(QWebEnginePage.WebAction.Reload).setText("刷新")
    web.pageAction(QWebEnginePage.WebAction.Stop).setText("停止加载")
    web.pageAction(QWebEnginePage.WebAction.Cut).setText("剪切")
    web.pageAction(QWebEnginePage.WebAction.Copy).setText("复制")
    web.pageAction(QWebEnginePage.WebAction.Paste).setText("粘贴")
    web.pageAction(QWebEnginePage.WebAction.Undo).setText("撤销")
    web.pageAction(QWebEnginePage.WebAction.Redo).setText("重做")
    web.pageAction(QWebEnginePage.WebAction.SelectAll).setText("全选")
    web.pageAction(QWebEnginePage.WebAction.OpenLinkInThisWindow).setText("在此标签页中打开链接")
    web.pageAction(QWebEnginePage.WebAction.OpenLinkInNewWindow).setText("在新窗口中打开链接")
    web.pageAction(QWebEnginePage.WebAction.OpenLinkInNewTab).setText("在新标签页中打开链接")
    web.pageAction(QWebEnginePage.WebAction.CopyLinkToClipboard).setText("复制链接")
    web.pageAction(QWebEnginePage.WebAction.DownloadLinkToDisk).setText("将链接另存为...")
    web.pageAction(QWebEnginePage.WebAction.CopyImageToClipboard).setText("复制图片")
    web.pageAction(QWebEnginePage.WebAction.CopyImageUrlToClipboard).setText("复制图片链接")
    web.pageAction(QWebEnginePage.WebAction.DownloadImageToDisk).setText("保存图片")
    web.pageAction(QWebEnginePage.WebAction.CopyMediaUrlToClipboard).setText("复制视频链接")
    web.pageAction(QWebEnginePage.WebAction.DownloadMediaToDisk).setText("保存视频")
    web.pageAction(QWebEnginePage.WebAction.Unselect).setText("反选")
    web.pageAction(QWebEnginePage.WebAction.SavePage).setText("保存网页")
    web.pageAction(QWebEnginePage.WebAction.ViewSource).setText("查看网页源代码")


