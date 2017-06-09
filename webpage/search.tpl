<!DOCTYPE html>

<html>
<head>
    <meta charset="utf-8">
    <title>Volvox - Responsive HTML5 Bootstrap Template</title>
    <meta name="keywords" content="HTML5 Template" />
    <meta name="description" content="Volvox - Responsive HTML5 Template">
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

<body>

    <!--Header-->
    <div class="header-container">



        <header class="header fixed clearfix">

            <div class="container">

                <!--Site Logo-->
                <div class="logo">
                    <a href="/index">
                        <img alt="Volvox" src="../webpage/img/logo.png" data-logo-height="35">
                    </a>
                </div>
                <!--End Site Logo-->

                <div class="navbar-collapse nav-main-collapse collapse">


                    <!--Main Menu-->
                    <nav class="nav-main mega-menu">
                        <ul class="nav nav-pills nav-main" id="mainMenu">

                            <li class="dropdown ">
                                <a class="dropdown-toggle" href="/index"><i class="fa fa-search"></i> Nouvelle Recherche</a>

                            </li>


                        </ul>
                    </nav>
                    <!--End Main Menu-->
                </div>
                <button class="btn btn-responsive-nav btn-inverse" data-toggle="collapse" data-target=".nav-main-collapse">
                    <i class="fa fa-bars"></i>
                </button>
            </div>
        </header>

    </div>
    <!--End Header-->

    <div id="container">

        <div class="v-page-wrap no-bottom-spacing">

            <!--Set your own slider options. Look at the v_RevolutionSlider() function in 'theme-core.js' file to see options-->
            <div class="container">
                <div class="row">
                    <div class="v-page-wrap no-top-spacing no-bottom-spacing">
						<div class="row fw-row">




							<div class="v-gmap-widget fullscreen-map col-sm-12">
								<div class="v-wrapper">
                                        <div id="googlemapsFullWidth" style="height:450px;"
                                             class="google-map mt-none mb-none"></div>
                                        <script>
                                            %
                                                var installations = []
                                                var i = 0
                                                for install in installation :
                                                   installations[i]=install
                                            % end
                                            alert(installations[1].nomInstall)

                                            function initMap() {
                                                var map = new google.maps.Map(document.getElementById('googlemapsFullWidth'), {
                                                    zoom: 4,
                                                    center: new google.maps.LatLng(47.1964374,-1.5731989),
                                                    clickableIcons: false
                                                });
                                                setMarkers(map, installations);
                                            }

                                            function setMarkers(map, installations){
                                                for(var i=0; i<installations.length; i++){
                                                    var install = installations[i];
                                                    alert("nom: "+install[0])
                                                    var myLatLng = new google.maps.LatLng(install[7], install[8]);
                                                    alert("ma longLat : "+myLatLng)
                                                    var infoWindow = new google.maps.InfoWindow();
                                                    var marker = new google.maps.Marker({
                                                        position : myLatLng,
                                                        map : map
                                                    });
                                                    (function(i){
                                                        google.maps.event.addListener(marker, "click", function () {
                                                            var install = installations[i];
                                                            infoWindow.close();
                                                            infoWindow.setContent('<div id="content">' +
                                                                '<h1 id="firstHeading" class="firstHeading">'+ install[0] +'</h1>' +
                                                                '<div id="bodyContent">' +
                                                                '<p>Adresse : <br/>'+install[5]+' '+ install[6] +'<br/>'+ install[2] +' '+install[3] ''<br/>' +'</p>'+
                                                                '<p>Nombre de places dans le parking : ' + install[10] +'</p>'+
                                                                '</div>');
                                                            infoWindow.open(map, this);
                                                        })
                                                    })(i);
                                                }
                                            }
                                            </script>
                                            <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
                                            </script>
                                            <script async defer
                                                    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDjeQGgnAwUgK0VgEHfOWArZ1mgVYiJvEQ&callback=initMap">
                                            </script>
                                        </div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>



            <!--<div class="container">
                <div class="row">
                    <div class="v-spacer col-sm-12 v-height-small"></div>
                </div>
            </div>-->

            <div class="container">

                <div class="row">

                    <div class="v-content-wrapper">

                        <div class="col-sm-12">

                            <div class="v-shadow-wrap center">

                                <div class="v-tagline-box v-tagline-box-v2 v-box-shadow shadow-effect-2">
                                    <h1><i class="fa fa-sort-up"></i>&nbsp;&nbsp;&nbsp;&nbsp;Veuillez selectionner une installation&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-sort-up"></i></h1>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


            <div class="container">
                <div class="v-spacer col-sm-12 v-height-mini"></div>
            </div>


            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="panel-group" id="accordion">
                            <div class="panel panel-default">

								<div class="panel-heading">
                                    <h4 class="panel-title">
                                        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseOne">
                                            <i class="fa fa-location-arrow"></i>
                                            Vision and Mission
                                        </a>
                                    </h4>
                                </div>
                                <div id="collapseOne" class="accordion-body collapse in">
                                    <div class="panel-body">
                                        Donec tellus massa, tristique sit amet condim vel, facilisis quis sapien.
                                        Praesent id enim sit amet odio vulputate eleifend in in tortor.
                                        Donec tellus massa, tristique sit amet condim vel.
                                    </div>
                                </div>
                            </div>
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    <h4 class="panel-title">
                                        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">
                                            <i class="fa fa-share"></i>
                                            Services we offer
                                        </a>
                                    </h4>
                                </div>
                                <div id="collapseTwo" class="accordion-body collapse">
                                    <div class="panel-body">
                                        Donec tellus massa, tristique sit amet condimentum vel, facilisis quis sapien.
                                    </div>
                                </div>
                            </div>
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    <h4 class="panel-title">
                                        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseThree">
                                            <i class="fa fa-flash"></i>
                                            Our Commitments
                                        </a>
                                    </h4>
                                </div>
                                <div id="collapseThree" class="accordion-body collapse">
                                    <div class="panel-body">
                                        Donec tellus massa, tristique sit amet condimentum vel, facilisis quis sapien.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <div class="container">
                <div class="v-spacer col-sm-12 v-height-big"></div>
            </div>

			<div class="container">
                <a href="/index"><button type="button"  class="btn v-btn v-belize-hole"><i class="fa fa-home"></i>RETOUR</button></a>
			</div>

        </div>

        </div>


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
</body>
</html>
