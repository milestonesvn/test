import sys
sys.path.append('../test')
import dl
net = dl.load_inception()
dl.convert_net(net, 'data/temp1')
net.save('convbnscale.caffemodel')
