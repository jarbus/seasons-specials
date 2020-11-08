import re

testpage = """
<!DOCTYPE html>

<html id="farmgroup" class="content">
<head>

    <title>Back Home Farm - LocalHarvest</title>

    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, shrink-to-fit=no">
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css"/>

    <!-- START pure.io styles -->
        <!--link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css"-->
        <link rel="stylesheet" href="//cdn.jsdelivr.net/pure/0.6.0/pure-min.css">
        <!--[if lte IE 8]>
            <link rel="stylesheet" href="/css/pureio/grid-old-ie.css">
        <![endif]-->
        <!--[if gt IE 8]><!-->
            <link rel="stylesheet" href="/css/pureio/grid.css">
        <!--<![endif]-->
        <link rel="stylesheet" type="text/css" href="/css/pureio/grid.css"/>
    <!-- END pure.io styles -->
    <link rel="stylesheet" type="text/css" href="/css/lh_main.css?52644209B97FB0D48BD024B89BDB9364"/>
    <link rel="stylesheet" type="text/css" href="/css/g.css"/>
    <link rel="stylesheet" type="text/css" href="/css/john.css"/>
    <!-- responsive queries -->
    <link rel="stylesheet" type="text/css" href="/css/lh_responsive.css"/>
    <!-- HTML5 shiv -->
    <!--[if lt IE 9]>
        <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.2/html5shiv.min.js"></script>
    <![endif]-->
    <script type="text/javascript">
      var _gaq = _gaq || [];
      var pluginUrl = '//www.google-analytics.com/plugins/ga/inpage_linkid.js';
      _gaq.push(['_setAccount', 'UA-85629-1']);
      _gaq.push(['_setDomainName', 'localharvest.org']);
      _gaq.push(['_require', 'inpage_linkid', pluginUrl]);
      _gaq.push(['_trackPageview']);
      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;

        ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
      var searchTypeParm = -1;
    </script>

    <!-- jQuery CDN with fallback to local /js/. Using 1.X for oldIE -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>
    if (typeof jQuery === 'undefined') {
        document.write(unescape("%3Cscript src='/js/jquery-1.11.3.min.js' type='text/javascript'%3E%3C/script%3E"));
        }
    </script>
    <script src="/js/jquery-ui.js"></script>
    <!-- Modernizr boxsizing - check for browser support, correct it if doesn't -->
    <script src="/js/modernizr.custom.69717.js" type="text/javascript"></script>
    <script>
        $(function(){
            if(!($('html').hasClass('boxsizing'))){
                $('html').each(function(){
                    //if($(this).css('display')=='block'){
                        var f, a, n;
                        f = $(this).outerWidth();
                        a = $(this).width();
                        n = a-(f-a);
                        $(this).css('width', n);
                    //}
                });
            }
        });
    </script>
    <script src="/js/localharvest.js" language="javascript"></script>
    <!-- doc ready MUST come after jQuery script has been loaded -->
    <script>
        $( document ).ready(function() {
            // $("#contentwrapper").css("width")
            width = window.innerWidth ? window.innerWidth : $(window).width();
            height = window.innerHeight ? window.innerHeight : $(window).height();
            $("#header").css("width",$("#header").parent().css("width"));
            // for mobile PS and remodal
            $(".pswp").css("width",width);
            $(".pswp").css("height",height);
            $(".pswp").find(".pswp__container").css("width",width);
            $(".remodal").css("width",width);
            $(".remodal").css("height",height);
            $(".remodal-wrapper").css("width",width);
            $(".remodal-wrapper").css("height",height);
        });

        $(window).on('resize', function(){
            waitForFinalEvent(function(){
                $("#header").css("width",$("#header").parent().css("width"));
                // for mobile PS and remodal
                $(".pswp").css("width",width);
                $(".pswp").css("height",height);
                $(".pswp").find(".pswp__container").css("width",width);
                $(".remodal").css("width",width);
                $(".remodal").css("height",height);
                $(".remodal-wrapper").css("width",width);
                $(".remodal-wrapper").css("height",height);
            }, 500, "headerResize");
        });

        var waitForFinalEvent = (function () {
            var timers = {};
            return function (callback, ms, uniqueId) {
                if (!uniqueId) {
                  uniqueId = "Don't call this twice without a uniqueId";
                }
                if (timers[uniqueId]) {
                  clearTimeout (timers[uniqueId]);
                }
                timers[uniqueId] = setTimeout(callback, ms);
            };
        })();
    </script>

    <script src="/js/ga_social_tracking.js" type="text/javascript"></script>

    <meta http-equiv="Content-Language" content="en">
    <meta property="fb:app_id" content="292617314171657" />

  <meta property="og:url" content="https://www.localharvest.org/back-home-farm-M45242" />
  <meta property="og:title" content="Back Home Farm - LocalHarvest" />
  <meta property="og:image" content="https://ded8b07dd9e637888fc2-e87978aaae5cf97349d88697fd53e4c9.ssl.cf1.rackcdn.com/30725.jpg" />

  <meta name="description" content="Back Home Farm is a local CSA farm in Weogufka, Alabama. LocalHarvest helps you find local, organic, farm-fresh food near you." />
  <meta name="keywords" content="Back Home Farm, Weogufka, Alabama, CSA,  farm, local food, organic" />
  <link rel="canonical" href="https://www.localharvest.org/back-home-farm-M45242" />
  <link rel="stylesheet" href="/css/photoswipe/photoswipe.css">
  <link rel="stylesheet" href="/css/photoswipe/default-skin/default-skin.css">
  <link rel="stylesheet" href="/css/remodal/jquery.remodal.css">

  <script>
      window.fbAsyncInit = function() {
          FB.init({
          appId      : '292617314171657',
          cookie     : true,
          xfbml      : true,
          version    : 'v2.9' // use graph api version 2.9
         });
      };
      (function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/en_US/all.js";
          fjs.parentNode.insertBefore(js, fjs);
      } (document, 'script', 'facebook-jssdk'));
      _ga.trackFacebook();
  </script>
  <script type="text/javascript">
    $(document).ready(function() {
        $('ul.tabs').each(function(){
          var $active, $content, $links = $(this).find('a');
          var defTab;
          if ($(this).attr('id') == 'seasons') {
            defTab = '#' + openTab;
          } else {
            defTab = location.hash;
          }
          $active = $($links.filter('[href="' + defTab + '"]')[0] || $links[0]);
          $active.parent().addClass('active');
          $content = $($active.attr('href'));
          $content.show();

          $links.not($active).each(function () {
            $($(this).attr('href')).hide();
          });

          $(this).on('click', 'a', function(e){
            $active.parent().removeClass('active');
            $content.hide();
            $active = $(this);
            $content = $($(this).attr('href'));
            $active.parent().addClass('active');
            $content.show();
            e.preventDefault();
          });
        });
    });
  </script>

</head>

<body>
  <div id="container">
    <div id="header">

          <div id="logo">
            <a href="/" title="Local Harvest - Real Food, Real Farmers, Real Community"></a>

            <span id="slogan" style="white-space: nowrap;">Real Food, Real Farmers, Real Community&#8480;</span>

          </div>

        <div id="headercontent"><!-- leave logo out for now -->


          <div class="loginblock">


            <span id="loggedout">
              <span class="signupbtn"><a href="/accounts/create.jsp" rel="nofollow">Sign Up</a></span>
              <span id="login" class="login"><a href="/accounts/" rel="nofollow">Log In</a></span>
            </span>


          </div>



              <div id="search">
                <form id="search-form" name="search-form" method="get" action="/getmap.jsp" rel="nofollow">

                      <span id="search-dropdown" class="button-search-categories">
                        <span id="searchbar-category">All</span>
                        <span class="downcaret">&#x25BC;</span>
                      </span>


                      <label class="searchwhat">What:</label>
                      <input class="searchtextinput searchwhat" id="search-text" type="text" name="nm"  placeholder="Farms, CSAs, Products..." maxlength="120">


                      <label class="searchwhere" id="searchlabel">Near:</label>
                      <input class="searchtextinput searchwhere" id="search-near" type="text" name="zip" maxlength="120" placeholder="City or Zip Code" value="Waltham, MA">


                      <select name="deptId" id="deptdropdown" class="deptdropdown">
                        <option value="0">Entire Catalog
                        <option value="76" >Bakery<option value="43" >Bulbs & Tubers<option value="17" >Chocolate & Desserts<option value="14" >Coffee & Teas<option value="34" >CSA<option value="23" >Dairy & Eggs<option value="62" >Flowers<option value="16" >Fruits<option value="2" >Fruits & Nuts<option value="13" >Gift Baskets<option value="24" >Grocery & Produce<option value="25" >Herbs & Health<option value="1" >Honey<option value="11" >Meats<option value="42" >Plants<option value="3" >Preserves<option value="4" >Syrups
                      </select>


                      <input type="submit" id="omnisearchbutton" class="button-search" name="omnisearchbutton" value="&nbsp;" onClick="document.forms['search-form'].submit();">
                      <span class="searchglasswrap" onClick="document.forms['search-form'].submit();"><span class="searchglass" name="omnisearchbutton"></span></span>


                  <input type="hidden" id="ty" name="ty" value="-1" />
                </form>
                <div class="clear"></div>


                <div id="navmenupalette" class="shadow" style="width:220px;">
                  <div class="upcaret">&#x25B2;</div>
                  <div class="one-half-disable" style="margin-left:10px!important;">
                    <h4>Local Food</h4>
                    <ul>
                      <li><a class="search-panel-cat" href="#" data-cat="0">Farms</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="1">Farmers Markets</a></li>
                      <li><a class="search-panel-cat" href="/search.jsp?ty=6" data-cat="6">CSA</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="2">Restaurants</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="3">Grocery/Co-op</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="9">U-Pick</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="10">Farm Stand</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="8">Wholesale</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="7">Meat Processors</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="-1">All</a></li>
                    </ul>
                  </div>
                  <div class="one-half-last">
                    <h4>Shop</h4>
                    <ul>
                      <li><a class="search-panel-cat" href="#" data-cat="5">Catalog</a></li>
                      <li><a class="search-panel-cat" href="#" data-cat="6">CSA</a></li>
                    </ul>
                    <br />
                    <h4>Popular Products</h4>
                    <ul>
                      <li><a class="search-panel-cat" href="/store/fruits.jsp?r=sp" data-cat="0">Citrus</a></li>
                      <li><a class="search-panel-cat" href="/store/fruits.jsp?r=sp&nm=passion" data-cat="0">Passion Fruit</a></li>
                      <li><a class="search-panel-cat" href="/store/fruits.jsp?r=sp" data-cat="0">Fruits</a></li>
                      <li><a class="search-panel-cat" href="/store/bulbs-tubers.jsp?r=sp" data-cat="0">Bulbs and Tubers</a></li>
                      <li><a class="search-panel-cat" href="/store/seeds.jsp?r=sp" data-cat="0">Seeds</a></li>
                      <li><a class="search-panel-cat" href="/store/nuts.jsp?r=sp" data-cat="0">Nuts</a></li>
                    </ul>
                  </div>
                </div>
              </div>


        <!-- main navigation -->
        <div id="nav">
          <ul class="nav">
            <li id="nav-home"><a href="/">Home</a></li>
            <li id="nav-shop"><a href="/store/">Shop</a></li>
            <li id="nav-csa"><a href="/csa/">CSA</a></li>
            <li id="nav-farms"><a href="/organic-farms/">Farms</a></li>
            <li id="nav-markets"><a href="/farmers-markets/">Farmers Markets</a></li>
            <li id="nav-events"><a href="/events.jsp">Events</a></li>
            <li id="nav-newsletter"><a href="/newsletter/">Newsletter</a></li>

            <li id="nav-photos"><a href="/album.jsp">Photos</a></li>
          </ul>

          <select name="dropdownnav" class="dropdownnav" onchange="location = this.options[this.selectedIndex].value;">
                <option value="#">Menu</option>
                <option value="/">Home</option>
                <option value="/store/">Shop</option>
                <option value="/csa/">CSA</option>
                <option value="/organic-farms/">Farms</option>
                <option value="/farmers-markets/">Farmers Markets</option>
                <option value="/events.jsp">Events</option>
                <option value="/newsletter/">Newsletter</option>
                <option value="/album.jsp">Photos</option>
            </select>
        </div>
        <div class="clear"></div>
        </div><!-- end headercontent -->
        <div>
            <a href="#" id="toggle" class="custom-toggle" onclick="toggle_visibility('headercontent');"><s class="bar"></s><s class="bar"></s><s class="bar"></s></a>
        </div>


    </div><!-- end header -->

    <div class="headershadow"></div>


    <div id="contentwrapper">

      <div id="leftcontentwrapper">






        <div class="leftsidebar">

                    <div id="sidebar_inseason" class="widget">
          	<h4>In Season</h4>
          	<a class="inseason" href="https://sharonsnaturalgardens.csaware.com/store/dept.jsp?m&did=18&p=2">
          		<h4>Garden Seeds</h4>
              <img src="https://64f3af98a19fcdc38cfe-39a6ad9c1a35b5ccf200eff7491ba20a.ssl.cf1.rackcdn.com/prod_6681_11620.V1.jpg" alt="Garden Seeds" />
          	</a>
          </div>


          
          <div class="widget">
          	<h4>Food & Farm Events</h4>
          	<table class="lhcalendar">
<tr><td align="left">
<a href="/events.jsp?y=2020&m=10"><span class="calendarnav">&laquo;</span></a>
</td><td align="center">Nov-2020</td>
<td align="right">
<a href="/events.jsp?y=2020&m=12"><span class="calendarnav">&raquo;</span></a></td>
</tr><tr><td colspan="3">
<table class="lhcaldays"><tr><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=1" class="calday">1</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=2" class="calday">2</a></td><td class="cal_active">3</td><td class="cal_active">4</td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=5" class="calday">5</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=6" class="calday">6</a></td><td class="cal_today"><a href="/events.jsp?y=2020&m=11&d=7" class="calday">7</a></td></tr><tr><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=8" class="calday">8</a></td><td class="cal_active">9</td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=10" class="calday">10</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=11" class="calday">11</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=12" class="calday">12</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=13" class="calday">13</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=14" class="calday">14</a></td></tr><tr><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=15" class="calday">15</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=16" class="calday">16</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=17" class="calday">17</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=18" class="calday">18</a></td><td class="cal_active">19</td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=20" class="calday">20</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=21" class="calday">21</a></td></tr><tr><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=22" class="calday">22</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=23" class="calday">23</a></td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=24" class="calday">24</a></td><td class="cal_active">25</td><td class="cal_active">26</td><td class="cal_active">27</td><td class="cal_active"><a href="/events.jsp?y=2020&m=11&d=28" class="calday">28</a></td></tr><tr><td class="cal_active">29</td><td class="cal_active">30</td><td class="cal_inactive">1</td><td class="cal_inactive">2</td><td class="cal_inactive">3</td><td class="cal_inactive">4</td><td class="cal_inactive">5</td></tr></table>
</td></tr>
</table>
          </div>




          <div class="widget">
            <div class="newsletter-sidebar">
              <h4 style="color: #176545;">LocalHarvest Newsletter</h4>
              <form method="post" action="/newslettersub_p.jsp">
                <input class="textinput" type="text" name="mail" maxlength="100" placeholder="email address" />
                <div class="clear"></div>
                <br />
                <input class="button-brand wide" type="submit" value="Sign Me Up" />
                <div class="clear"></div>
              </form>
            </div>
          </div>





          <div id="sidebar_connect" class="widget">
            <h4>Connect</h4>
            <br />
            <div class="socialchicklets" style="margin-left:10px;">
              <ul>
                <li><a class="social-facebook" href="https://www.facebook.com/LocalHarvest"></a></li>
                <li><a class="social-twitter" href="https://twitter.com/localharvestorg"></a></li>
                <li><a class="social-instagram" href="https://www.instagram.com/localharvest.org_/"></a></li>
              </ul>
            </div>
            <div class="clear"></div>
          </div>

        </div>




        <div id="content">


<div id="fb-root"></div>
<div class="fullwidth">
  <div class="left" style="max-width:355px;">

    <h1 class="inline">Back Home Farm</h1>
    <br />
    <span style="font-size:14px; font-weight:bold; line-height:24px;">
      <a href="/search.jsp?lat=32.928856&lon=-86.40439&scale=12&zip=35183" rel="nofollow">Weogufka, Alabama</a>
    </span>

    <br />
    <i><a href="/organic-farms/">Family Farm</a></i>

  </div>


  <div class="right">

    <div class="left">

      <div class="left">

            <img src="/images/stars-0.png" width="69" height="12" vspace="4" align="absmiddle" border="0"></a>

      </div>


      <div class="left" style="margin-left:15px;">
        <div class="fb-like fb_iframe_widget" >
          <div class="fb-like" data-href="http://www.localharvest.org/back-home-farm-M45242"
                data-send="false" data-layout="button_count" data-width="100" data-show-faces="false"></div>
        </div>
      </div>

    </div>
    <div class="clear"></div>
    <br />
    <span class="button button-default"><a href="/new-review.jsp?rev&mid=45242" rel="nofollow">Post a Review</a></span>
    <a href="/listing_email.jsp?id=45242" class="nl inline right" rel="nofollow"><span class="icon icon-envelope"></span> Email this</a>
    <div class="clear"></div>
    <br />
    <div class="clear"></div>
  </div>


  <div class="clear"></div>
</div>

<br />






<div class="left fullwidth" style="max-width: 600px;">


  <div class="">

    <div class="listingdesc ">
      <div class="left" style="margin:0 15px 10px 0;">



        <div class="shadow open-lightbox" style="margin-left:auto;margin-right:auto;width:250px;height:250px;overflow:hidden;">
            <figure itemprop="associatedMedia" itemscope itemtype="https://schema.org/ImageObject">
                  <a href="https://ded8b07dd9e637888fc2-e87978aaae5cf97349d88697fd53e4c9.ssl.cf1.rackcdn.com/30725.jpg" class="photo_0" itemprop="contentUrl" data-size="600x400" data-index="0" data-caption="" data-filename="30725">
                    <div style="width:250px;height:250px;overflow:hidden;position:relative;">
                      <img src="https://ded8b07dd9e637888fc2-e87978aaae5cf97349d88697fd53e4c9.ssl.cf1.rackcdn.com/30725_300.jpg" id="mbrimg" title="Back Home Farm" alt="Back Home Farm" style="position: absolute;
  left: 50%;
  top: 50%;
  height: 100%;
  width: auto;
  -webkit-transform: translate(-50%,-50%);
      -ms-transform: translate(-50%,-50%);
          transform: translate(-50%,-50%);" />
        </div>
                  </a>
            </figure>
        </div>




      </div>

      <div id="descDiv">
        <p>Back Home Farm is a small scale farm committed to growing food sustainably for the surrounding community and region.  A sustainable farm requires that we make stewardship of the soil and the farm's natural resources our top priority.  We are also committed to our community...we desire to provide fresh, locally grown produce to citizens of central Alabama at competitive prices. We also hope to regularly provide and serve the needs of local residents by donating produce to local food shelters and ministries that are centered in Coosa, Talladega, and Tallapoosa Counties.   We started farming in 2011 and have approximately 25 varieties of vegetables, including some heirloom and open pollinated cultivars.  This year, we have initiated our CSA program and registration is open until March 1 (please call after March 1 for last-minute openings).  The CSA program will serve Sylacauga, Birmingham, north Atlanta, and possibly other locations.  Details can be found on the "Our Harvest" link of our website: backhomefarm.com.  </p><p>In addition, we've added fresh eggs to our production (available March 15th 2012) as well as including shiitake and oyster mushrooms (available September 2012).  Other future products will include grass fed goat, sheep, and cattle.
      </div>

    </div>
  </div>


  <div class="clear"></div>
  <i>Listing last updated on <span class="oldListingAlert">Mar 22, 2013</span></i>
  <br />
  <br />



  <hr />
  <div class="listingFeature">
    <p>2013 CSA Registration is Open Now!  Deliveries begin in April!</p>
  </div>
  <br />







  <div class="">




    <ul class="tabs" id="outlets">

      <li><a href="#O1">CSA</a></li>

      <li><a href="#O2">Farmers' Market</a></li>

    </ul>


    <div class="tabs-content">

      <div id="O1" class="tab-panel" style="display:block;">


        <div class="fullwidth">
          <div class="col one-half">
            <p>
              <span class="inlineblock" style="width:80px;"><b>Season:</b></span>
              &nbsp;<span class="inline">May through August</span>
            </p>
            <p>
              <span class="inlineblock" style="width:80px;"><b>Type:</b></span>
              &nbsp;<span class="inline">single farm</span>
            </p>

            <p>
              <span class="inlineblock" style="width:80px;"><b>Since:</b></span>
              &nbsp;<span class="inline">2012</span>
            </p>


            <p>
              <span class="inlineblock" style="width:80px;"><b># of Shares:</b></span>
              &nbsp;<span class="inline">75</span>
            </p>

          </div>
          <div class="col one-half">

            <p>
              <span class="inlineblock" style="width:80px;"><b>Share Prices:</b></span>
              &nbsp;<span class="inline">full share: $30/week for 18 weeks.  </span>
            </p>

            <p>
              <span class="inlineblock" style="width:80px;"><b>Work Req?</b></span>
              &nbsp;<span class="inline">No</span>
            </p>
          </div>
          <div class="clear"></div>
        </div>

        <input type="button" class="button button-brand right" style="width:180px;" onclick="window.location='/back-home-farm-M45242/csa'" value="More CSA Details" /><br />

        <div class="clear"></div>
      </div>

      <div id="O2" class="tab-panel" >


            <div>


              <h4>Markets on LocalHarvest</h4>
              <br />

              <i>Know a market serving this farm? Tell them to connect here on LocalHarvest!</i>

            </div>

            <br />


        <b>Schedule and Location:</b><br />
        <p>Markets for this year have not been confirmed yet.  Please check back later for market locations and dates. Thanks!</p>

        <div class="clear"></div>
      </div>

    </div>
  </div>
  <br />






  <br />


  <div>
    <h4>Latest Reviews</h4>

    <div class="clear"></div>

    <span class="button button-default right" style="padding-right:20px;"><a href="/new-review.jsp?rev&mid=45242" rel="nofollow">Post a Review</a></span>
    <p>No reviews available.  Be the first!</p>

  </div>
  <hr />
  <br />







    <div class="fullwidth">
      <h4>Products and Crops <a href="/products.jsp" target="_blank" alt="Learn More" title="Learn More" ><span class="icon icon-info"></span></a></h4>
      <br />

      <ul class="tabs" id="seasons">

        <li id="tabSpring"><a href="#Spring">Spring</a></li>

        <li id="tabSummer"><a href="#Summer">Summer</a></li>

        <li id="tabFall"><a href="#Fall">Fall</a></li>

      </ul>

      <div class="tabs-content">

        <div class="tab-panel" id="Spring">
          <h5>Spring</h5>
          <br />

          <div class="col one-third perfect">
            <div class="one-third-inner">
              <h6>Vegetables:</h6>
              <ul>

                <li><a href="/broccoli.jsp">broccoli</a></li>

                <li><a href="/carrots.jsp">carrots</a></li>

                <li><a href="/chinese-greens.jsp">chinese greens</a></li>

                <li><a href="/collards.jsp">collards</a></li>

                <li><a href="/cucumber.jsp">cucumber</a></li>

                <li><a href="/kale.jsp">kale</a></li>

                <li><a href="/lettuce.jsp">lettuce</a></li>

              </ul>
            </div>
          </div>
          <div class="col one-third perfect">
            <div class="one-third-inner">
              <ul>

                <li><a href="/onions.jsp">onions</a></li>

                <li><a href="/peas.jsp">peas</a></li>

                <li><a href="/potatoes.jsp">potatoes</a></li>

                <li><a href="/radishes.jsp">radishes</a></li>

                <li><a href="/salad-greens.jsp">salad greens</a></li>

                <li><a href="/chard.jsp">swiss chard</a></li>

                <li><a href="/turnips.jsp">turnips</a></li>

              </ul>
              <br />

              <h6>Meats/Livestock:</h6>
              <ul>

                <li><a href="/organic-chicken.jsp">chicken</a></li>

              </ul>
            </div>
          </div>
          <div class="col one-third perfect">
            <div class="one-third-inner">
              <ul>

              <h6>Dairy/Eggs:</h6>
              <ul>

                <li><a href="/pastured-eggs.jsp">eggs</a></li>

              </ul>
              <br />

              <h6>Herbs:</h6>
              <ul>

                <li>fresh herbs</li>

              </ul>
            </div>
          </div>
        </div>

        <div class="tab-panel" id="Summer">
          <h5>Summer</h5>
          <br />

          <div class="col one-third perfect">
            <div class="one-third-inner">
              <h6>Vegetables:</h6>
              <ul>

                <li><a href="/carrots.jsp">carrots</a></li>

                <li><a href="/sweet-corn.jsp">sweet corn</a></li>

                <li><a href="/cucumber.jsp">cucumber</a></li>

                <li><a href="/eggplant.jsp">eggplant</a></li>

                <li><a href="/garlic.jsp">garlic</a></li>

                <li><a href="/green-beans.jsp">green beans</a></li>

                <li><a href="/hot-peppers.jsp">hot peppers</a></li>

                <li><a href="/lettuce.jsp">lettuce</a></li>

                <li><a href="/okra.jsp">okra</a></li>

                <li><a href="/peas.jsp">peas</a></li>

                <li><a href="/potatoes.jsp">potatoes</a></li>

                <li><a href="/salad-greens.jsp">salad greens</a></li>

                <li><a href="/summer-squash.jsp">summer squash</a></li>

                <li><a href="/sweet-peppers.jsp">sweet peppers</a></li>

              </ul>
            </div>
          </div>
          <div class="col one-third perfect">
            <div class="one-third-inner">
              <ul>

                <li><a href="/sweet-potato.jsp">sweet potatoes</a></li>

                <li><a href="/tomatillos.jsp">tomatillos</a></li>

                <li><a href="/tomatoes.jsp">tomatoes</a></li>

                <li><a href="/winter-squash.jsp">winter-squash</a></li>

                <li><a href="/zucchini.jsp">zucchini</a></li>

              </ul>
              <br />

              <h6>Fruits:</h6>
              <ul>

                <li><a href="/blackberries.jsp">blackberries</a></li>

                <li><a href="/blueberries.jsp">blueberries</a></li>

                <li><a href="/cantaloupes.jsp">cantaloupes</a></li>

                <li><a href="/melons.jsp">melons</a></li>

                <li><a href="/watermelons.jsp">watermelons</a></li>

              </ul>
              <br />

              <h6>Meats/Livestock:</h6>
              <ul>

                <li><a href="/organic-chicken.jsp">chicken</a></li>

              </ul>
              <br />

              <h6>Dairy/Eggs:</h6>
              <ul>

                <li><a href="/pastured-eggs.jsp">eggs</a></li>

              </ul>
            </div>
          </div>
          <div class="col one-third perfect">
            <div class="one-third-inner">
              <ul>

              <h6>Processed:</h6>
              <ul>

                <li><a href="/pickles.jsp">pickles</a></li>

              </ul>
              <br />

              <h6>Herbs:</h6>
              <ul>

                <li>fresh herbs</li>

              </ul>
              <br />

              <h6>Flowers:</h6>
              <ul>

                <li><a href="/organic-flowers.jsp">fresh flowers</a></li>

              </ul>
              <br />

              <h6>Specialty Items:</h6>
              <ul>

                <li>hay / straw</li>

              </ul>
            </div>
          </div>
        </div>

        <div class="tab-panel" id="Fall">
          <h5>Fall</h5>
          <br />

          <div class="col one-third perfect">
            <div class="one-third-inner">
              <h6>Vegetables:</h6>
              <ul>

                <li><a href="/broccoli.jsp">broccoli</a></li>

                <li><a href="/collards.jsp">collards</a></li>

                <li><a href="/kale.jsp">kale</a></li>

                <li><a href="/onions.jsp">onions</a></li>

                <li><a href="/peas.jsp">peas</a></li>

              </ul>
            </div>
          </div>
          <div class="col one-third perfect">
            <div class="one-third-inner">
              <ul>

                <li><a href="/pumpkins.jsp">pumpkins</a></li>

                <li><a href="/turnips.jsp">turnips</a></li>

                <li><a href="/winter-squash.jsp">winter-squash</a></li>

              </ul>
              <br />

              <h6>Meats/Livestock:</h6>
              <ul>

                <li><a href="/organic-chicken.jsp">chicken</a></li>

                <li><a href="/ostrich.jsp">ostrich</a></li>

              </ul>
            </div>
          </div>
          <div class="col one-third perfect">
            <div class="one-third-inner">
              <ul>

              <h6>Dairy/Eggs:</h6>
              <ul>

                <li><a href="/pastured-eggs.jsp">eggs</a></li>

              </ul>
              <br />

              <h6>Specialty Items:</h6>
              <ul>

                <li>hay / straw</li>

              </ul>
            </div>
          </div>
        </div>

        <script type="text/javascript">var openTab='Fall';</script>
        <div class="clear"></div>
      </div>
    </div>
    <br />
    <br />







  <div class="clear"></div>
  <br />
  <br />
</div>
<!-- END left -->
</div>


</div>



<div class="right sidebar">
  <div class="center">
    <div class="callout center" style="max-width:220px;">
      <a href="/keepmeposted.jsp?zip=54812" class="nl" rel="nofollow" title="Keep Up-to-date on Farm News from This Area"><span class="icon icon-bookmark"></span> KeepMePosted on farms and events in this area</a>
    </div>

  </div>
  <br />



  <!-- Right Sidebar Top -->
  <div id="div-gpt-ad-1411421866207-1">
    <script type="text/javascript">
      googletag.cmd.push(function() { googletag.display('div-gpt-ad-1411421866207-1'); });
    </script>
  </div>
  <!-- Right Sidebar 2nd from Top -->
  <div id="div-gpt-ad-1417558888159-0">
    <script type="text/javascript">
      googletag.cmd.push(function() { googletag.display('div-gpt-ad-1417558888159-0'); });
    </script>
  </div>



  <div class="panel center" style="max-width:280px;">
    <div style="text-align:left;">
      <h3 class="subheading">Contact Information</h3>
      <br />

      <div class="tab">
        <h5>Contact</h5>
        <div>
          <span>Andy Whorton</span><br />
          <span>(256) 245-7628</span>
        </div>
      </div>
      <br />


      <div class="tab">
        <h5>Location</h5>
        <div>
          13374 Coosa County Road 29<br />

          Weogufka, AL 35183

        </div>
      </div>
      <br />



      <div class="tab">
        <h5>Mailing Address</h5>
        <div>
          13374 Coosa County Road 29<br />

          Weogufka, AL 35183
        </div>
      </div>
      <br />


      <div class="tab">

        <a href="http://www.backhomefarm.com" target="_blank" rel="nofollow">www.backhomefarm.com <span class="icon icon-outlink"></span></a>
        <br />
        <br />


        <a href="http://www.facebook.com/backhome.farm" target="_blank"><img src="/images/fbook_18.png" border="0" hspace="1" vspace="3"></a>


        <a href="https://twitter.com/backhomefarm" target="_blank"><img src="/images/twit_18.png" border="0" hspace="1" vspace="3"></a>



      </div>
      <br />

      <div class="center">

        <span class="button button-default left">
          <a href="/postemail.jsp?id=45242" rel="nofollow">Email Us</a>
        </span>

        <span class="button button-default right">
          <a href="http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=13374+Coosa+County+Road+29,+Weogufka+AL+35183" target="_blank">Get Directions</a>
        </span>

      </div>
      <div class="clear"></div>
    </div>
  </div>
  <br />



  <div class="panel center callout" style="max-width:280px;">
    <div style="text-align:left;">
      <h3 class="subheading">Coming Events</h3>
      <br />

      <b>No Events on File</b>
      <br />

      <br />
      <a href="/events.jsp?zip=35183&amp;rad=100" rel="nofollow" class="right"><b>See all events for this area....</b></a>
      <div class="clear"></div>
    </div>
  </div>
  <br />



  <!-- START gallery -->
  <div class="panel center" style="max-width:280px;">
    <h3 class="subheading" style="text-align:left;">Photos</h3>
    <div class="picture" itemscope itemtype="https://schema.org/ImageGallery">
      <!-- START responsive grid -->
      <div class="pure-g">

        <div class="puregrid-unit-1 puregrid-unit-sm-1-2 puregrid-unit-md-1-4">
          <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
            <div style="padding:4px;">
              <a href="https://ded8b07dd9e637888fc2-e87978aaae5cf97349d88697fd53e4c9.ssl.cf1.rackcdn.com/30725.jpg" class="photo_0" itemprop="contentUrl" data-size="255x245" data-index="0" data-caption=" " data-filename="30725">
                <img class="pure-img center" src="https://ded8b07dd9e637888fc2-e87978aaae5cf97349d88697fd53e4c9.ssl.cf1.rackcdn.com/30725_180x180.jpg" height="180" width="180" itemprop="thumbnail" alt=" " />
              </a>
            </div>
          </figure>
        </div>

      </div>
      <!-- END responsive grid -->
    </div>
    <div class="clear"></div>
    <div class="right">
      <a href="/photos.jsp?id=45242">More Photos</a>
    </div>
    <br />
  </div>
  <!-- END gallery -->
  <br />



  <div class="panel center" style="max-width:280px;">
    <div style="text-align:left;">
      <h3 class="subheading">Additional Information</h3><br />


              <div class="">

          <h5>Farming Practices</h5>

          <ul>

            <li><a href="/organic.jsp#naturallygrown">naturally grown</a></li>

            <li><a href="/organic.jsp#pastured">grass fed/pastured</a></li>

            <li><a href="/organic.jsp#ipm">integrated pest management</a></li>

          </ul>

        </div>

      <br />


      <div class="">

        <h5>Association Memberships</h5>

        <ul>

          <li><a href="/org.jsp?id=40">Southern SAWG (SSAWG)</a></li>

        </ul>

      </div>

    </div>
  </div>
  <br />



  <div class="panel center" style="max-width:280px;">
    <div style="text-align:left;">
      <h3 class="subheading">Nearby Cities</h3><br />

<ul>
<li><a href="/sylacauga-al/">Sylacauga, AL</a></li><li><a href="/prattville-al/">Prattville, AL</a></li><li><a href="/alabaster-al/">Alabaster, AL</a></li><li><a href="/montgomery-al/">Montgomery, AL</a></li><li><a href="/talladega-al/">Talladega, AL</a></li><li><a href="/vestavia-hills-al/">Vestavia Hills, AL</a></li><li><a href="/birmingham-al/">Birmingham, AL</a></li>
</ul>


    </div>
  </div>



</div>





<!-- START PhotoSwipe lightbox markup -->
<div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="pswp__bg"></div>
    <div class="pswp__scroll-wrap">

        <div class="pswp__container">
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
        </div>

        <div class="pswp__ui pswp__ui--hidden">
            <div class="pswp__top-bar">
                <div class="pswp__counter"></div>
                <div class="pswp_buttonmenu">
                    <button class="pswp__button pswp__button--close" title="Close (Esc)"></button>
                    <button class="pswp__button pswp__button--share" title="Share"></button>
                    <button class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button>
                    <button class="pswp__button pswp__button--zoom" title="Zoom in/out"></button>
                    <!-- logged in overlay menu buttons -->

                </div>
                <div class="pswp__preloader">
                    <div class="pswp__preloader__icn">
                      <div class="pswp__preloader__cut">
                        <div class="pswp__preloader__donut"></div>
                      </div>
                    </div>
                </div>
            </div>
            <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
                <div class="pswp__share-tooltip"></div>
            </div>
            <button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)">
            </button>
            <button class="pswp__button pswp__button--arrow--right" title="Next (arrow right)">
            </button>
            <div class="pswp__caption">
                <div class="pswp__caption__center"></div>
            </div>
        </div>
    </div>
</div>
<!-- END PhotoSwipe overlay markup -->

<script src="/js/jquery.remodal.min.js"></script>
<script src="/js/photoswipe.min.js"></script>
<script src="/js/photoswipe-ui-default_custom.js"></script>


<!-- Other scripts -->
<script type="text/javascript">
    (function($)
    {
        var $pswp = $('.pswp')[0];
        var lightBox;
        var image = [];

        $('div.picture').each( function() {
            var $pic = $(this),
            getItems = function()
            {
                var items = [];
                $pic.find('a').each(function()
                {
                    var $href   = $(this).attr('href'),
                        $caption = $(this).data('caption'),
                        $filename = $(this).data('filename'),
                        $size = $(this).data('size').split('x'),
                        $width  = $size[0],
                        $height = $size[1];

                    var item =
                    {
                        src : $href,
                        w   : $width,
                        h   : $height,
                        title : $caption,
                        file : $filename
                    }

                    items.push(item);
                });
                return items;
            }

            var items = getItems();

            $.each(items, function(index, value)
            {
                image[index]     = new Image();
                image[index].src = value['src'];
            });

            $pic.on('click', 'figure', function(event)
            {
                event.preventDefault();

                var options =
                {
                    index: $(this).find("a").data("index"),
                    bgOpacity: 0.7,
                    showHideOpacity: true
                }

                lightBox = new PhotoSwipe($pswp, PhotoSwipeUI_Default, items, options);
                lightBox.init();
            });

            $( '.open-lightbox' ).on('click', 'figure', function(event)
            {
                event.preventDefault();

                var options =
                {
                    index: $(this).find("a").data("index"),
                    bgOpacity: 0.7,
                    showHideOpacity: true
                }

                lightBox = new PhotoSwipe($pswp, PhotoSwipeUI_Default, items, options);
                lightBox.init();
            });
        });

        // ajax setup
        $.ajaxSetup({
            crossDomain: true,
            xhrFields: { withCredentials: true }
        });

        // admin tools function calls - these need tap calls too, though
        $( "#delete-photo-confirm" ).click(function() { deletePhoto(); });
        $( "#caption-confirm" ).click(function() { editCaption(); });
        $( "#profile-photo-confirm" ).click(function() { setProfilePhoto(); });
        $( "#add-listing-confirm" ).click(function() { event.preventDefault();$("#addListing").submit(); });

        // PhotoSwipe admin tools menu button functions
        function deletePhoto() {
            $.post("https://" + window.location.hostname + "/members/photo_p.jsp?del=" + lightBox.currItem.file, function(data) {
                lightBox.items.splice(lightBox.getCurrentIndex(),1);
                lightBox.invalidateCurrItems();
                lightBox.updateSize(true);
                $("a[data-index='" + lightBox.getCurrentIndex() + "']").parent().parent().parent().remove();
            });
        }

        function editCaption() {
            var caption = $('#new-caption').val().trim();
            if (caption != lightBox.currItem.caption) {
                $.post("https://" + window.location.hostname + "/members/photo_p.jsp?cap=" + lightBox.currItem.file + "&text=" + caption, function(data) {
                    lightBox.currItem.title = caption;
                    $('.pswp__caption__center').html(caption);
                });
            }
        }

        function setProfilePhoto() {
            $.post("https://" + window.location.hostname + "/members/photo_p.jsp?main=" + lightBox.currItem.file, function(data) {
                window.location.href = window.location.href.split("#")[0];
            });
        }

    })(jQuery);
</script>

<script type="text/javascript">
    var $el, $ps, $up, totalHeight;

    $(".listingdesc .moreLink").click(function() {
        totalHeight = 20
        $el = $(this);
        $p  = $el.parent();
        $up = $p.parent();
        $ps = $up.find("p:not('.readmore'), li, br");
        $lis = $up.find("li");
        $ps.each(function() {
            totalHeight += ($(this).outerHeight()) + 18;
        });
        $up
            .css({
                "height": $up.height(),
                "max-height": 9999
            })
            .animate({
                "height": totalHeight
            });
        $p.fadeOut();
        return false;
    });
</script>


      <div class="clear"></div>


      <div class="center" style="margin-top:0; padding-top:10px;border-top:1px solid #c7c7c7;">
        <div id="ld-5284-2800" class="center"></div>
<script>(function(w,d,s,i){w.ldAdInit=w.ldAdInit||[];w.ldAdInit.push({slot:9948241521532774,size:[0, 0],id:"ld-5284-2800"});if(!d.getElementById(i)){var j=d.createElement(s),p=d.getElementsByTagName(s)[0];j.async=true;j.src="//cdn2.lockerdomecdn.com/_js/ajs.js";j.id=i;p.parentNode.insertBefore(j,p);}})(window,document,"script","ld-ajs");</script>
      </div>


    </div>

  </div>

  <div class="clear"></div>

  <div id="footer">
    <div class="footer-one">
      <div class="pure-g">
      <div class="puregrid-unit-1 puregrid-unit-md-1-4" style="float:left;"> <!-- prev .footer-fourth-width -->
        <ul>
          <li><h2>Quick Links</h2></li>
          <li><a href="/">Home</a></li>
          <li><a href="/locations/">Local Food Near You</a></li>
          <li><a href="/events.jsp">Events Calendar</a></li>
          <li><a href="https://www.csaware.com">CSAware</a></li>
        </ul>
      </div>
      <div class="puregrid-unit-1 puregrid-unit-md-1-4" style="float:left;">
        <ul>
          <li><h2>Support</h2></li>
          <li><a href="https://help.localharvest.org" rel="nofollow">Help / Knowledge Base</a></li>
          <li><a href="/contact.jsp" rel="nofollow">Contact Us</a></li>
          <li><a href="/about.jsp">About Us</a></li>
          <li><a href="/privacy.jsp" rel="nofollow">Privacy</a></li>
          <li><a href="/legal.jsp" rel="nofollow">Terms & Conditions</a></li>
          <li><a href="/media.jsp">Press & Outreach</a></li>
        </ul>
      </div>
      <div class="puregrid-unit-1 puregrid-unit-md-1-4" style="float:left;">
        <ul>
          <li><h2>Connect With Us</h2></li>
          <li><a href="/newsletter/">Newsletter</a></li>
          <li><a href="/blog/all/">Blogs</a></li>
          <li><a href="/album.jsp">Farm Photos</a></li>
          <li>
            <div class="socialchicklets">
              <ul>
                <li><a class="social-facebook" href="http://www.facebook.com/LocalHarvest" rel="nofollow"></a></li>
                <li><a class="social-twitter" href="http://twitter.com/localharvestorg" rel="nofollow"></a></li>
                <li><a class="social-instagram" href="https://www.instagram.com/localharvest.org_/" rel="nofollow"></a></li>
              </ul>
            </div>
          </li>
        </ul>
      </div>
      <div class="puregrid-unit-1 puregrid-unit-md-1-4" style="float:left;">
        <ul>
          <li><h2>Shop</h2></li>
          <li><a href="/accounts/" rel="nofollow">My Account</a></li>
          <li><a href="/store/">Online Store</a></li>
          <li><a href="/products.jsp">Farm Products</a></li>
		</ul>
      </div>
      </div><!-- end pureg -->
      <div class="clear"></div>

      <div class="locs">
        <ul class="locs">
          <li><a href="/atlanta-ga">Atlanta</a></li>
          <li><a href="/austin-tx">Austin</a></li>
          <li><a href="/boston-ma">Boston</a></li>
          <li><a href="/chicago-il">Chicago</a></li>
          <li><a href="/dallas-tx">Dallas</a></li>
          <li><a href="/denver-co">Denver</a></li>
          <li><a href="/detroit-mi">Detroit</a></li>
          <li><a href="/honolulu-hi">Honolulu</a></li>
          <li><a href="/houston-tx">Houston</a></li>
          <li><a href="/los-angeles-ca">Los Angeles</a></li>
          <li><a href="/memphis-tn">Memphis</a></li>
          <li><a href="/miami-fl">Miami</a></li>
          <li><a href="/minneapolis-mn">Minneapolis</a></li>
          <li><a href="/new-york-ny">New York</a></li>
          <li><a href="/philadelphia-pa">Philadelphia</a></li>
          <li><a href="/phoenix-az">Phoenix</a></li>
          <li><a href="/portland-or">Portland</a></li>
          <li><a href="/sacramento-ca">Sacramento</a></li>
          <li><a href="/san-diego-ca">San Diego</a></li>
          <li><a href="/san-francisco-ca">San Francisco</a></li>
          <li><a href="/san-jose-ca">San Jose</a></li>
          <li><a href="/seattle-wa">Seattle</a></li>
          <li><a href="/washington-dc">Washington, DC</a></li>
          <li><a href="/locations">More Cities</a></li>
        </ul>

        <select name="locations" class="locations" onchange="location = this.options[this.selectedIndex].value;">
            <option value="#">Locations</option>
            <option value="/atlanta-ga">Atlanta</option>
            <option value="/austin-tx">Austin</option>
            <option value="/boston-ma">Boston</option>
            <option value="/chicago-il">Chicago</option>
            <option value="/dallas-tx">Dallas</option>
            <option value="/denver-co">Denver</option>
            <option value="/detroit-mi">Detroit</option>
            <option value="/honolulu-hi">Honolulu</option>
            <option value="/houston-tx">Houston</option>
            <option value="/los-angeles-ca"><a href="/los-angeles-ca">Los Angeles</a></option>
            <option value="/memphis-tn"><a href="/memphis-tn">Memphis</a></option>
            <option value="/miami-fl"><a href="/miami-fl">Miami</a></option>
            <option value="/minneapolis-mn"><a href="/minneapolis-mn">Minneapolis</a></option>
            <option value="/new-york-ny"><a href="/new-york-ny">New York</a></option>
            <option value="/philadelphia-pa"><a href="/philadelphia-pa">Philadelphia</a></option>
            <option value="/phoenix-az"><a href="/phoenix-az">Phoenix</a></option>
            <option value="/portland-or"><a href="/portland-or">Portland</a></option>
            <option value="/sacramento-ca"><a href="/sacramento-ca">Sacramento</a></option>
            <option value="/san-diego-ca"><a href="/san-diego-ca">San Diego</a></option>
            <option value="/san-francisco-ca"><a href="/san-francisco-ca">San Francisco</a></option>
            <option value="/san-jose-ca"><a href="/san-jose-ca">San Jose</a></option>
            <option value="/seattle-wa"><a href="/seattle-wa">Seattle</a></option>
            <option value="/washington-dc"><a href="/washington-dc">Washington, DC</a></option>
            <option value="/locations"><a href="/locations">More Cities</a></option>
        </select>
      </div>


      <div class="center" style="margin-top:10px;">
        <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1532853216720182" data-ad-slot="7922194788"></ins>
        <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script>
      </div>


    </div>

    <div class="footer-two">
      <span class="footleft"><p>Copyright &copy; 1999-2020 LocalHarvest, Inc.</p></span>
      <span class="footright">
        <ul class="footer-links">
          <li><a href="/privacy.jsp" rel="nofollow">Privacy Policy</a></li>
          <li><a href="/legal.jsp" rel="nofollow">Terms</a></li>
        </ul>
      </span>
    </div>

  </div>


    <!-- for responsive nav -->
    <script type="text/javascript">
    <!--
        function toggle_visibility(id) {
           var e = document.getElementById(id);
           if(e.style.display == 'block')
              e.style.display = 'none';
           else
              e.style.display = 'block';
        }
    //-->
    </script>
</body>
</html>
"""

testpage = testpage.replace("\n"," ")
locblock = re.search(r"<h5>Location</h5>(.*?)</div>",testpage).group(1)
address = re.sub(r'<.*?>','',locblock)
address = re.sub(r'\s\s+',' ',address).strip()
print(locblock)
print(address)
