import re, plistlib
# 1) Giữ màn hình luôn sáng
f = 'ios/App/App/AppDelegate.swift'
s = open(f).read()
s = re.sub(r'(didFinishLaunchingWithOptions[^\n]*\{\n)',
           r'\1        UIApplication.shared.isIdleTimerDisabled = true\n', s, count=1)
open(f, 'w').write(s)
# 2) Ẩn thanh trạng thái
f = 'ios/App/App/Info.plist'
d = plistlib.load(open(f, 'rb'))
d['UIStatusBarHidden'] = True
d['UIViewControllerBasedStatusBarAppearance'] = False
d['UIRequiresFullScreen'] = True
plistlib.dump(d, open(f, 'wb'))
print('patched ios')
