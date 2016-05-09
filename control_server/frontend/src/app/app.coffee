angular.module('arduinoBattle', [
    'ngResource'
    'ngSanitize'
    'ngRoute'
    'ngAnimate'

    'ui.bootstrap'

    'swUtils'
    'swWebSocket'
])


.config ($routeProvider) ->
    $routeProvider
        .when('/',
          templateUrl: 'controllers/main.html'
          controller: 'MainCtrl'
          label: ''
        )
        .when('/car/:id/',
          templateUrl: 'controllers/car.html'
          controller: 'CarCtrl'
          label: 'Car'
        )
        .when('/create_car/',
          templateUrl: 'controllers/create_car.html'
          controller: 'CreateCarCtrl'
          label: ''
        )
        .otherwise('/')

.run ($location, $rootScope, swTitle) ->
    $rootScope.swTitle = swTitle
    $rootScope.$on '$routeChangeSuccess', (event, current, previous) ->
        baseTitle = current.$$route?.label or ''
        swTitle.setTitleBase(baseTitle)
        swTitle.setTitleStart('')
        swTitle.setTitleEnd('')


.config ($httpProvider) ->
#    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'

    $httpProvider.defaults.xsrfCookieName = 'csrftoken'
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'

.config ($resourceProvider) ->
    $resourceProvider.defaults.stripTrailingSlashes = false;

