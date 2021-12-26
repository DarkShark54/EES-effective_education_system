import windowstypes as tw


app = tw.Authorization()
if app.data != 0:
    tw.mainwindow(app.data)
