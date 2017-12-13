import wx

app = wx.App()
screen = wx.ScreenDC()
size = screen.GetSize()

def Get():
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC()
    mem.SelectObject(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    mem.SelectObject(wx.NullBitmap)
    img = bmp.ConvertToImage()
    #bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
    del mem
    return bmp
