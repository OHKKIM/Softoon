<?php
$str = file_get_contents('/home/ubuntu/softoon/comment.json');
$star = json_decode($str, true);
$hate = json_decode($str, true);
$like = json_decode($str, true);
$t1=0;
$t2=0;
$t3=0;
$t4=0;
$t5=0;
$t6=0;
usort($star, function($string1, $string2){
	return $string1['star'] < $string2['star'];
});
usort($like, function($string1, $string2){
	return $string1['like'] < $string2['like'];
});
usort($hate, function($string1, $string2){
	return $string1['hate'] < $string2['hate'];
});
?>
<!doctype html>
<html>
	<head>
		<title>Softoon</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="is-preload">
            <!-- Header -->
                <header id="header">
                    <a class="logo" href="softoon.php">Softoon</a>
                </header>

            <!-- Banner -->
                <section id="banner">
                    <div class="inner">
		    <h1>Softoon</h1>
                        <p>오늘의 핫한 Naver 웹툰<br />
                        copyright by <a href="https://comic.naver.com/index.nhn">Naver Webtoon</a></p>
                    </div>
                    <video autoplay loop muted playsinline src="images/banner.mp4"></video>
                </section>

            <!-- Highlights -->
                <section class="wrapper">
                    <div class="inner">
                        <header class="special">
                            <h2 id = "time-result"></h2>
			    <p style="font-size:1.5em;">웹툰 별점 TOP 6</p>
                        </header>
                        <div class="highlights">
                            <section>
                                <div class="content">
                                    <header style="font-size:2em;">TOP 1</header>
				    <a style="text-decoration:none;" href="<?php echo$star[$t1]['url'] ?>">
					<img src="<?php echo$star[$t1]['img'] ?>" width="250" height="202"><br>
				    	<span style="font-size:1em; color:black;"><?php echo$star[$t1]['title'] ?>&nbsp;&nbsp;&nbsp;★<?php echo$star[$t1]['star'] ?></span>
				    </a>
				</div>
                            </section>
                            <section>
                                <div class="content">
				    <header style="font-size:2em;">TOP 2</header>
				    <?php
					for($i=1;$i<200;$i++) if($star[$i]['url']!=$star[$t1]['url']) {$t2=$i; break;}
				    ?>
				    	<a style="text-decoration:none;" href="<?php echo$star[$t2]['url'] ?>">
                                        <img src="<?php echo$star[$t2]['img'] ?>" width="250" height="202"><br>
					<span style="font-size:1em; color:black;"><?php echo$star[$t2]['title'] ?>&nbsp;&nbsp;&nbsp;★<?php echo$star[$t2]['star'] ?></span>
					</a>
				</div>
		            </section>
		    	    <section>
				<div class="content">
			    	    <header style="font-size:2em;">TOP 3</header>
				    <?php
					for($i=1;$i<200;$i++) if($star[$i]['url']!=$star[$t1]['url']) if($star[$i]['url']!=$star[$t2]['url']) {$t3=$i; break;}
				    ?>                                     
                                    	<a style="text-decoration:none;" href="<?php echo$star[$t3]['url'] ?>">
				    	<img src="<?php echo$star[$t3]['img'] ?>" width="250" height="202"><br>
					<span style="font-size:1em; color:black;"><?php echo$star[$t3]['title'] ?>&nbsp;&nbsp;&nbsp;★<?php echo$star[$t3]['star'] ?></span>
					</a>
				</div>
			    </section>
			    <section>
				<div class="content">
				    <header style="font-size:2em;">TOP 4</header>
				    <?php
					for($i=1;$i<200;$i++) if($star[$i]['url']!=$star[$t1]['url']) if($star[$i]['url']!=$star[$t2]['url'])
					if($star[$i]['url']!=$star[$t3]['url']) {$t4=$i; break;}
				    ?>
					<a style="text-decoration:none;" href="<?php echo$star[$t4]['url'] ?>">
                                        <img src="<?php echo$star[$t4]['img'] ?>" width="250" height="202"><br>
                                        <span style="font-size:1em; color:black;"><?php echo$star[$t4]['title'] ?>&nbsp;&nbsp;&nbsp;★<?php echo$star[$t4]['star'] ?></span>
                        	        </a>
                                </div>
                            </section>
                            <section>
                                <div class="content">
				    <header style="font-size:2em;">TOP 5</header>
				    <?php
					for($i=1;$i<200;$i++) if($star[$i]['url']!=$star[$t1]['url']) if($star[$i]['url']!=$star[$t2]['url'])
					if($star[$i]['url']!=$star[$t3]['url']) if($star[$i]['url']!=$star[$t4]['url']) {$t5=$i; break;}
				    ?>
                                	<a style="text-decoration:none;" href="<?php echo$star[$t5]['url'] ?>">
                                        <img src="<?php echo$star[$t5]['img'] ?>" width="250" height="202"><br>
                                        <span style="font-size:1em; color:black;"><?php echo$star[$t5]['title'] ?>&nbsp;&nbsp;&nbsp;★<?php echo$star[$t5]['star'] ?></span>
                                        </a>
                                </div>
                            </section>
                            <section>
                                <div class="content">
				    <header style="font-size:2em;">TOP 6</header>
				    <?php
					for($i=1;$i<200;$i++) if($star[$i]['url']!=$star[$t1]['url']) if($star[$i]['url']!=$star[$t2]['url'])
					if($star[$i]['url']!=$star[$t3]['url']) if($star[$i]['url']!=$star[$t4]['url']) if($star[$i]['url']!=$star[$t5]['url']){$t6=$i; break;}
				    ?>
                                    	<a style="text-decoration:none;" href="<?php echo$star[$t6]['url'] ?>">
                                        <img src="<?php echo$star[$t6]['img'] ?>" width="250" height="202"><br>
					<span style="font-size:1em; color:black;"><?php echo$star[$t6]['title'] ?>&nbsp;&nbsp;&nbsp;★<?php echo$star[$t6]['star'] ?></span>
                                    	</a>
                                </div>
                            </section>
                        </div>
                    </div>
                </section>

            <!-- CTA -->
                <section id="cta" class="wrapper">
                    <div class="inner">
                        <h2>오늘의 댓글</h2>
			<p style="margin:2rem;">좋아요</p>
			<a style="font-size:1em; text-decoration:none; color:white;" href="<?php echo$like[0]['url'] ?>">
			<?php echo$like[0]['content'] ?><br>
			Likes :  <?php echo$like[0]['like'] ?>&nbsp;&nbsp;&nbsp;Hates :  <?php echo$like[0]['hate'] ?></a><br>
			<p style="margin:2rem;">싫어요</p>
			<a style="font-size:1em; text-decoration:none; color:white;" href="<?php echo$hate[0]['url'] ?>">
                        <?php echo$hate[0]['content'] ?><br>
                        Likes :  <?php echo$hate[0]['like'] ?>&nbsp;&nbsp;&nbsp;Hates :  <?php echo$hate[0]['hate'] ?></a><br>
                    </div>
                </section>

            <!-- Footer -->
                <footer id="footer">
                    <div class="inner">
                        <div class="content">
                            <section>
                                <h3>Cloud Computing Project</h3>
				<p>AWS EC2를 활용한 Naver Webtoon Comment Crawling
				그날의 웹툰 업로드를 보여주며 댓글, 별점을 통해 핫한 웹툰을 안내한다.</p>
                            </section>
                            <section>
                                <h4>충북대학교</h4>
                                <ul class="alt">
                                    <li><a href="https://software.cbnu.ac.kr">충북대 소프트웨어학과</a></li>
                                    <li><a href="http://cslab.cbnu.ac.kr/class.php?sem=2019.2&id=cc">Cloud Computing (Fall, 2019)</a></li>
                                </ul>
                            </section>
                            <section>
                                <h4>Git</h4>
                                <ul class="plain">
                                    <li><a href="https://github.com/dltkddnr0058/Softoon"><i class="icon fa-github">&nbsp;</i>Github</a></li>
                                </ul>
                            </section>
                        </div>
                        <div class="copyright">
                            &copy; Webtoon <a href="https://comic.naver.com/index.nhn">NAVER</a>, HTML Template <a href="https://templated.co/industrious">TEMPLATED</a>.
                        </div>
                    </div>
                </footer>

            <!-- Scripts -->
                <script src="assets/js/jquery.min.js"></script>
                <script src="assets/js/browser.min.js"></script>
                <script src="assets/js/breakpoints.min.js"></script>
                <script src="assets/js/util.js"></script>
                <script src="assets/js/main.js"></script>
		<script type="text/javascript">
                    var d = new Date();
		    var week = new Array('일', '월', '화', '수', '목', '금', '토');
		    var currentDate = d.getFullYear()+"년 "+(d.getMonth()+1)+"월 "+d.getDate()+"일 "+week[d.getDay()]+"요일";
		    var result = document.getElementById("time-result");
		    result.innerHTML = currentDate;
		</script>
	</body>
</html>
