import windowstypes as tw


app = tw.Authorization()
if app.data:
    tw.mainwindow(app.data)
