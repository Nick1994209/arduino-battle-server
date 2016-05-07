angular.module('arduinoBattle')

.service('userService', (UserResource) -> 
    self = this
    this.getUsername = () ->
      UserResource.query({},
        ((data) ->
          self.user = data['username']
        ),
        ((errors) ->
            console.log(errors)
        )
      )
)