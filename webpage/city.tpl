<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8">

    <title>SPORT-FINDER</title>
    <meta name="keywords" content="SPORT-FINDER" />
    <meta name="description" content="SPORT-FINDER">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="shortcut icon" type="image/png" href="../webpage/img/favicon.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Web Fonts  -->
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,500,600,700,800" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Raleway:100,200,300,400,500,700,800,900" rel="stylesheet" type="text/css">


    <!-- Libs CSS -->
    <link href="../webpage/css/bootstrap.min.css" rel="stylesheet" />
    <link href="../webpage/css/style.css" rel="stylesheet" />
    <link href="../webpage/css/font-awesome.min.css" rel="stylesheet" />
    <link href="../webpage/css/streamline-icon.css" rel="stylesheet" />
    <link href="../webpage/css/v-nav-menu.css" rel="stylesheet" />
    <link href="../webpage/css/v-portfolio.css" rel="stylesheet" />
    <link href="../webpage/css/v-blog.css" rel="stylesheet" />
    <link href="../webpage/css/v-animation.css" rel="stylesheet" />
    <link href="../webpage/css/v-bg-stylish.css" rel="stylesheet" />
    <link href="../webpage/css/v-shortcodes.css" rel="stylesheet" />
    <link href="../webpage/css/theme-responsive.css" rel="stylesheet" />
    <link href="../webpage/plugins/owl-carousel/owl.theme.css" rel="stylesheet" />
    <link href="../webpage/plugins/owl-carousel/owl.carousel.css" rel="stylesheet" />

    <!-- Current Page CSS -->
    <link href="../webpage/plugins/rs-plugin/css/settings.css" rel="stylesheet" />
    <link href="../webpage/plugins/rs-plugin/css/custom-captions.css" rel="stylesheet" />

    <!-- Custom CSS -->
    <link rel="stylesheet" href="../webpage/css/custom.css">
</head>

<body class="floating-header">




    <div id="container" class="slideshow">

        <!--Set your own slider options. Look at the v_RevolutionSlider() function in 'theme-core.js' file to see options-->
        <div class="home-slider-wrap fullwidthbanner-container" >
            <form id="formulaire" data-toggle="validator" role="form" action="/activity" method="POST">
            <div class="v-rev-slider" data-slider-options='{ "fullScreen":"on", "fullScreenOffsetContainer": ".fw-slider-spacer" }' style="background-color: #21C2F8;">
                <ul>
                    <!-- SLIDE  -->
                    <li data-transition="fade" data-slotamount="7" data-masterspeed="1000">
                        <!-- MAIN IMAGE -->
                        <!--<img src="img/image2.png" alt="fullslide6" data-start="0" data-speed="0" data-bgposition="center top" data-bgfit="cover" data-bgrepeat="no-repeat">-->
                        <!-- LAYERS -->

                        <div class="tp-caption light_heavy_50 sfl stl"
                            data-x="435"
                            data-y="0"
                            data-speed="0"
                            data-start="0"
                            data-easing="Power1.easeInOut"
                            data-splitin="none"
                            data-splitout="none"
                            data-elementdelay="0"
                            data-endelementdelay="0"
                            data-endspeed="300">
                            <i class="fa fa-soccer-ball-o"></i>&nbsp;SPORT-FINDER
                        </div>

                        <div class="tp-caption v-caption-h1 sfl stl"
                            data-x="500"
                            data-y="60"
                            data-speed="0"
                            data-start="0"
                            data-easing="Power1.easeInOut"
                            data-splitin="none"
                            data-splitout="none"
                            data-elementdelay="0"
                            data-endelementdelay="0"
                            data-endspeed="300">
                            Trouvez les équipements<br>
                            sportifs près de chez vous.
                        </div>

						<div class="tp-caption sfl stl"
                            data-x="500"
                            data-y="200"
                            data-speed="0"
                            data-start="0"
                            data-easing="Power1.easeInOut"
                            data-splitin="none"
                            data-splitout="none"
                            data-elementdelay="0"
                            data-endelementdelay="0"
                            data-endspeed="300">

							<div class="row">
								<div class="col-md-4 form-group">

									<input id="zip" name="zip" type="text" placeholder="Zip" class="form-control" maxlength="5" value="{{zip}} " readonly="readonly">
								</div>

								<div id="div_ville" class="col-md-8">
                                    <!--<select class="form-control" disabled="">-->
                                    <select id="select_ville" name="select_ville" class="form-control">

                                        % for ville in liste_ville:
                                            <option>{{ville}}</option>
                                        % end
                                    </select>
								</div>


							</div>
						</div>

                        <div class="tp-caption sfl stl"
                            data-x="500"
                            data-y="370"
                            data-speed="0"
                            data-start="0"
                            data-easing="Power1.easeInOut"
                            data-splitin="none"
                            data-splitout="none"
                            data-elementdelay="0"
                            data-endelementdelay="0"
                            data-endspeed="300">
                            <button type="submit" id="btn_suivant" class="btn v-btn v-second-light"><i class="fa fa-play"></i> SUIVANT</button>
                        </div>

                        <div class="tp-caption sfl stl"
                            data-x="700"
                            data-y="370"
                            data-speed="0"
                            data-start="0"
                            data-easing="Power1.easeInOut"
                            data-splitin="none"
                            data-splitout="none"
                            data-elementdelay="0"
                            data-endelementdelay="0"
                            data-endspeed="300">
                            <a href='/index' id="btn_new" class="btn v-btn v-second-light"><i class="fa fa-refresh"></i> NOUVELLE RECHERCHE </a>

                        </div>


                    </li>


                </ul>
            </div>
            </form>
            <div class="shadow-right"></div>
		</div>



    <!--// BACK TO TOP //-->
    <div id="back-to-top" class="animate-top"><i class="fa fa-angle-up"></i></div>

    <!-- Libs -->
    <script src="../webpage/js/jquery.min.js"></script>
    <script src="../webpage/js/bootstrap.min.js"></script>
    <script src="../webpage/js/jquery.flexslider-min.js"></script>
    <script src="../webpage/js/jquery.easing.js"></script>
    <script src="../webpage/js/jquery.fitvids.js"></script>
    <script src="../webpage/js/jquery.carouFredSel.min.js"></script>
    <script src="../webpage/js/jquery.validate.js"></script>
    <script src="../webpage/js/theme-plugins.js"></script>
    <script src="../webpage/js/jquery.isotope.min.js"></script>
    <script src="../webpage/js/imagesloaded.js"></script>

    <script src="../webpage/js/view.min.js?auto"></script>

    <script src="../webpage/plugins/rs-plugin/js/jquery.themepunch.tools.min.js"></script>
    <script src="../webpage/plugins/rs-plugin/js/jquery.themepunch.revolution.min.js"></script>

    <script src="../webpage/js/theme-core.js"></script>

    <script>
		$(document).ready(function() {

			$('#btn_suivant').click(function () {

            });

		});

	</script>



</body>
</html>
