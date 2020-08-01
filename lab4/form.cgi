#!/usr/bin/perl

use CGI;
use CGI ':standard';
use strict;

print "Content-type: text/html\n\n";
print "<link rel='stylesheet' type='text/css' href='../css/lab4.css'>\n";
print "<h1 class='mario-font'>Mario Survey</h1>\n";

print "<br>\n";

my $first = param("txtFirst");
my $last = param("txtLast");
my $age = param("txtAge");
my $gender = param("radGender");
my $mario = param("gameSel");

print "<div class=content>";
print "<p>Why is everything I do Mario-based?</p> <br>";
print "Hi there, $first $last! ";
print "You are $age years old, and your gender is $gender. <br>";

if ($mario eq "SM64") {
	print "Your favourite 3D Mario game is Super Mario 64. <br><br>";
	print "This was Mario's first time adventuring in a 3D world. The graphics haven't aged well at all, but the rose-tinted glasses I'm wearing help hide that.<br><br>";
	print "This game is such timeless classic. I bet you're always quick going up the stairs. <br><br>";
	print "<img src='../img/blj.gif'>"
}
elsif ($mario eq "SMS") {
	print "Your favourite 3D Mario game is Super Mario Sunshine. <br><br>";
	print "I'm guessing you'd much rather be lounging on a tropical island right about now.<br><br>";
	print "Just hope your arch-nemesis' son hasn't kidnapped your girlfriend because he was tricked into thinking she was his mother and that YOU'RE the one who kidnapped her. <br>";
	print "Man, Bowser really is a horrible father.<br><br>";
	print "<img src='../img/sunglasses.gif'>"
}
elsif ($mario eq "SMG") {
	print "Your favourite 3D Mario game is Super Mario Galaxy. <br><br>";
	print "Funnily enough, it's also my favourite!<br>";
	print "There's something about this game that sets it apart from all the others in the series.<br>";
	print "It has a quiet and subtle story, and the dark emptiness of space drives home the feeling of hopelessness that Mario must be feeling.<br>";
	print "How is one little plumber going to take on the entire universe?<br><br>";
	print "<img src='../img/galaxy.gif'>"
}
elsif ($mario eq "SMG2") {
	print "Your favourite 3D Mario game is Super Mario Galaxy 2. <br><br>";
	print "Did you know that this game was created from leftover and cut ideas from Galaxy 1? <br><br>";
	print "This is also the reason the game has a much lighter tone and a more straightforward approach to level design compared to the first.<br><br>";
	print "Still just as good as the first game, though, because this time Mario has his own spaceship shaped like his face. Can't top that.<br><br>";
	print "<img src='../img/galaxy2.png' width='100%'>"
}
elsif ($mario eq "SM3L") {
	print "Your favourite 3D Mario game is Super Mario 3D Land. <br><br>";
	print "This is the only 3D Mario game on a handheld system. As such, the hardware limitations were pretty severe. <br>";
	print "This game did away with the large, exploration-based worlds of the previous 3D games, and used a structure similar to the 2D Mario games, with a linear level with only one goal: get to the end.<br><br>";
	print "The linear nature of 3D Land was controversial to some, but it created a sort of sub-genre of 3D Mario games.<br><br>";
	print "Oh, and Mario gets a fursuit. Can't forget that.<br><br>";
	print "<img src='../img/3dland.png' width='70%'>";
}
elsif ($mario eq "SM3W") {
	print "Your favourite 3D Mario game is Super Mario 3D World. <br><br>";
	print "The first 3D Mario game to be in HD. People had high expectations for this game, wanting another grand adventure, like a Galaxy 3 or Sunshine 2. <br>";
	print "Instead, we got another linear game like 3D Land, which was only a little bit disappointing. The levels were fun and a lot more interesting to explore, owning to the improved hardware, but they were still linear.<br><br>";
	print "And yup, we got more fursuits. This seemed to be a trend at Nintendo in the early 2010s.<br><br>";

	print "<img src='../img/3dworld.png' width='70%'>";
}
elsif ($mario eq "SMO") {
	print "Your favourite 3D Mario game is Super Mario Odyssey. <br><br>";
	print "After 7 years, 3D Mario returned to the large and immersive worlds, and the exploration-based playstyle that has defined the series in it's early years.<br><br>";
	print "This adventure saw Mario exploring the world and its many different kingdoms alongside his friend-turned-hat, Cappy.<br>";
	print "With Cappy's help, Mario can \"capture\" enemies and take control of them, allowing for many new gameplay mechanics that the series desperately needed.<br><br>";
	print "Oh, and the game is gorgeous. I mean, just look at it!<br><br>";

	print "<img src='../img/smo.gif' width='70%'>";
}
print "</div>";