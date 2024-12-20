# ldpc_code

refer to [https://github.com/hichamjanati/pyldpc](https://github.com/hichamjanati/pyldpc)

运行结果
```text
H Matrix:
 [[1 1 1 0 0 0 1 0]
 [0 0 0 1 1 1 0 1]
 [1 1 1 0 0 0 1 0]
 [0 0 0 1 1 1 0 1]]
G Matrix:
 [[1 0 0 0 0 0]
 [0 1 0 0 0 0]
 [0 0 1 0 0 0]
 [0 0 0 1 0 0]
 [0 0 0 0 1 0]
 [0 0 0 0 0 1]
 [1 1 1 0 0 0]
 [0 0 0 1 1 1]]
原始消息:
 [0 1 1 0 1 1]
编码后的码字:
 [ 1.42689032 -0.83203386 -1.15114035  1.25594786 -2.57501045  0.39611087
  1.21193894  1.44951218]
高斯噪声:
 [-0.10350391  1.05251704 -0.31538591  0.25739229 -1.73747627  0.67186916
  1.00858942  0.75440892]
接收到的信号:
 [ 1.32338641  0.22048318 -1.46652626  1.51334015 -4.31248672  1.06798004
  2.22052837  2.2039211 ]
解码后的消息:
 [0 1 1 0 1 1]
解码成功，消息一致！
```
