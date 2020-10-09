# internet-over-morse
A way to transmit webpages via morse code

Well this was an idea that I not a long time ago. Useless and pretty crazy, but when I looked into it a little bit more, I realized that it was not that difficult to make.
So I opened up Vim and wrote two little Python programs, an encoder and a decoder, and then I set up an HTTP livestream of the sound output of the computer which was encoding.
Just a little experiment, very slow but it works, so that's enough!
A little video: https://youtu.be/a7YOWXlUSWg

## How do I use this?
Well, first you can choose **not** to use it. But if you're sure, then you have to have those things:
**1.** multimon-ng on your decoder machine, which **has** to be a Linux machine, however you'll experience many problems, I think...
**2.** https://github.com/sunny256/cwwav to generate the morse code. It has to be above (in the upper directory) the Python files and needs to be already compiled.
**3.** VLC on your host machine. I used Windows 10 v.2004 with the Ubuntu subsystem, with https://www.streamwhatyouhear.com/ to stream the audio over HTTP (you see why it's completely useless now), but this could be also done I think with a VoIP phone if the compression is not too heavy. If you want to use the program on pure Linux, then you'll have to modify the code a little bit, but nothing complicated, it's fairly easy.
**4.** Python (of course!) on your Ubuntu subsystem (it should already be there) and in your decoder machine.
**5.** Well I think that's all... But I sure forgot one I think. Well I'll come back if I remember.

Enjoy!
