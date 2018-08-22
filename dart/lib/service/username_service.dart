library security_monkey.username_service;

import '../util/constants.dart';
import 'package:angular/angular.dart';
import 'dart:async';
import 'dart:html';
import '../model/Role.dart';

@Injectable()
class UsernameService {

    String name = "";
    Scope scope;
    List roles = new List();

    UsernameService(Scope scope) {
        //http://stackoverflow.com/questions/22151427/how-to-communicate-between-angular-dart-controllers
      Stream username_change_stream = scope.on('username-change');
      username_change_stream.listen(usernameChange);

      Stream roles_change_stream = scope.on('roles-change');
      roles_change_stream.listen(rolesChange);

        Stream authurl_change_stream = scope.on('authurl-change');
        authurl_change_stream.listen(authURLChange);
    }

    void authURLChange(ScopeEvent e) {
        String auth_url = e.data;
        if (auth_url.isNotEmpty) {
            if (REMOTE_AUTH) {
                window.location.assign(auth_url);
            } else {
                var url = Uri.encodeComponent(window.location.href);
                window.location.assign('/login?next=$url');
            }
        }
    }

    void usernameChange(ScopeEvent e) {
        this.name = e.data;
    }

    void rolesChange(ScopeEvent e) {
      this.roles = new List();
      for(Map role in e.data){
        this.roles.add(new Role.fromMap(role));
      }
    }

    get signed_in => name.isNotEmpty;

    bool isAdmin(){
      return hasRole("admin");
    }

    bool hasRole(String name){
      for (Role role in roles){
        if (role.id == name){
          return true;
        }
      }
      return false;
    }
}


//  // sender
//  scope.emit("username-change", "emit");
//  scope.broadcast("username-change", "broadcast");
//  scope.parentScope.broadcast("username-change", "parent-broadcast");
//  scope.rootScope.broadcast("username-change", "root-broadcast");
//
//  scope.$emit('my-event-name', [someData, someOtherData]); // propagate towards root
//  scope.$broadcast('my-event-name', [someData, someOtherData]); // propagate towards leaf nodes (children)
//  scope.$parent.$broadcast('my-event-name', [someData, someOtherData]); // send to parents childs (includes silblings children)
//  scope.$root.$broadcast('my-event-name', [someData, someOtherData]); // propagate towards leaf nodes starting from root (all nodes)
//
//  // receiver
//  scope.$on('my-event-name', (ScopeEvent e) => myCallback(e)); // call myCallback when an `my-event-name` event reaches me
