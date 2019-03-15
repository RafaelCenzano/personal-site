{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano - Raf{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/">

{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/home.css') }}>

	<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Montserrat:100">

{% endblock %}

{% block content %}

	<div id="app">
		<div id="glitch-wrapper">
			<!-- Make sure data-text equals the text you put inside the tags. -->
			<h1 class="glitch" data-text="Rafael Cenzano">Rafael Cenzano</h1>
		</div>
	</div>
	<div class="flip-container" ontouchstart="this.classList.toggle('hover');">
		<div class="flipper">
			<div class="front">
		    	<img src={{ url_for('static', filename='img/profile.jpeg') }} alt="Rafael Cenzano's Profile Image" class="profile">
			</div>
			<div class="back">
		    	<img src="https://www.python.org/static/community_logos/python-powered-h.svg" alt="Rafael Cenzano's Profile Image" class="profile">
			</div>
		</div>
	</div>


{% endblock %}
