(window.webpackJsonp=window.webpackJsonp||[]).push([[11],{J4zT:function(e,t,c){"use strict";c.r(t),c.d(t,"GroupModule",(function(){return A}));var n=c("3Pt+"),i=c("M0ag"),o=c("tyNb"),a=c("ey9i"),r=c("H+bZ"),s=c("D0Ju"),l=c("ntpF"),d=c("QDJC"),b=c("fXoL"),u=c("1kSV"),p=c("sYmb"),h=c("5eHb"),m=c("lDzL"),L=c("ZOsW"),g=c("ximh");const f=["table"],w=["content"];function v(e,t){if(1&e){const e=b.Ub();b.Lc(0,"\n                "),b.Tb(1,"i",22),b.ec("click",(function(){b.Bc(e);const c=t.row;return b.ic().delete(c)})),b.jc(2,"translate"),b.Sb(),b.Lc(3,"\n              ")}2&e&&(b.Ab(1),b.pc("title",b.kc(2,1,"group.create.delete.button")))}function S(e,t){1&e&&b.Lc(0),2&e&&b.Nc("\n                ",t.row._GroupId,"\n              ")}function T(e,t){if(1&e){const e=b.Ub();b.Lc(0,"\n                "),b.Tb(1,"input",23),b.ec("change",(function(c){b.Bc(e);const n=t.row;return b.ic().updateValue(c,n._GroupId)})),b.Sb(),b.Lc(2,"\n              ")}if(2&e){const e=t.row;b.Ab(1),b.oc("value",e.GroupName)}}function k(e,t){if(1&e&&(b.Lc(0,"\n                    "),b.Tb(1,"span",26),b.Lc(2,"\n                      "),b.Tb(3,"b"),b.Lc(4,"Widget"),b.Sb(),b.Lc(5),b.Tb(6,"b"),b.Lc(7,"IEEE"),b.Sb(),b.Lc(8),b.Tb(9,"b"),b.Lc(10,"Ep"),b.Sb(),b.Lc(11),b.Tb(12,"b"),b.Lc(13,"Id"),b.Sb(),b.Lc(14),b.Tb(15,"b"),b.Lc(16),b.Sb(),b.Lc(17,"\n                    "),b.Sb(),b.Lc(18,"\n                  ")),2&e){const e=t.item,c=t.searchTerm;b.Ab(1),b.oc("ngOptionHighlight",c),b.Ab(4),b.Nc(" : ",e.Name," - "),b.Ab(3),b.Nc(" : ",e.IEEE," - "),b.Ab(3),b.Nc(" : ",e.Ep," -\n                      "),b.Ab(3),b.Nc(" : ",e._ID," -\n                      "),b.Ab(2),b.Mc(e.ZDeviceName)}}function N(e,t){if(1&e){const e=b.Ub();b.Lc(0,"\n                "),b.Tb(1,"ng-select",24),b.ec("ngModelChange",(function(c){return b.Bc(e),t.row.devicesSelected=c}))("change",(function(){return b.Bc(e),b.ic().isFormValid()})),b.Lc(2,"\n                  "),b.Jc(3,k,19,6,"ng-template",25),b.Lc(4,"\n                "),b.Sb(),b.Lc(5,"\n              ")}if(2&e){const e=t.row,c=b.ic();b.Ab(1),b.oc("items",c.devices)("multiple",!0)("closeOnSelect",!1)("searchable",!0)("ngModel",e.devicesSelected)}}function I(e,t){if(1&e){const e=b.Ub();b.Lc(0,"\n                "),b.Tb(1,"div",27),b.Lc(2,"\n                  "),b.Tb(3,"input",28),b.ec("click",(function(c){b.Bc(e);const n=t.row;return b.ic().updateCoordinator(c,n)})),b.Sb(),b.Lc(4,"\n                "),b.Sb(),b.Lc(5,"\n              ")}if(2&e){const e=t.row;b.Ab(3),b.oc("checked",e.coordinatorInside)}}function E(e,t){1&e&&(b.Lc(0,"\n  "),b.Tb(1,"div",29),b.Lc(2,"\n    "),b.Ob(3,"h4",30),b.Lc(4,"\n    "),b.Tb(5,"button",31),b.ec("click",(function(){return t.$implicit.dismiss("Cross click")})),b.Lc(6,"\n      "),b.Tb(7,"span",32),b.Lc(8,"\xd7"),b.Sb(),b.Lc(9,"\n    "),b.Sb(),b.Lc(10,"\n  "),b.Sb(),b.Lc(11,"\n  "),b.Ob(12,"div",33),b.Lc(13,"\n  "),b.Tb(14,"div",34),b.Lc(15,"\n    "),b.Tb(16,"button",35),b.ec("click",(function(){return t.$implicit.dismiss("cancel")})),b.Sb(),b.Lc(17,"\n  "),b.Sb(),b.Lc(18,"\n"))}const x=new a.c("GroupComponent"),y=[{path:"",component:(()=>{class e extends d.a{constructor(e,t,c,n,i,o){super(),this.modalService=e,this.apiService=t,this.formBuilder=c,this.translate=n,this.toastr=i,this.headerService=o,this.rows=[],this.rowsTemp=[],this.temp=[],this.hasEditing=!1,this.waiting=!1}ngOnInit(){this.apiService.getZGroupDevicesAvalaible().subscribe(e=>{const t=[];e&&e.length>0&&(e.forEach(e=>{e.WidgetList.forEach(c=>{if("0000"!==e._NwkId){const n=new s.a;n.Ep=c.Ep,n.IEEE=c.IEEE,n.Name=c.Name,n.ZDeviceName=c.ZDeviceName,n._ID=c._ID,n._NwkId=e._NwkId,t.push(n)}})}),this.devices=[...t],this.getGroups())})}updateValue(e,t){this.hasEditing=!0,this.rows.find(e=>e._GroupId===t).GroupName=e.target.value}updateFilter(e){const t=e.target.value.toLowerCase(),c=this.temp.filter((function(e){let c=!1;return e._GroupId&&(c=-1!==e._GroupId.toLowerCase().indexOf(t)),!c&&e.GroupName&&(c=-1!==e.GroupName.toLowerCase().indexOf(t)),c||!t}));this.rows=c,this.table.offset=0}updateDevices(){this.rows.forEach(e=>{e.coordinatorInside&&(e.devicesSelected||(e.devicesSelected=[]),e.devicesSelected.push({Ep:"01",_NwkId:"0000"}))}),this.isFormValid&&this.apiService.putZGroups(this.rows).subscribe(e=>{x.debug(this.rows),this.hasEditing=!1,this.toastr.success(this.translate.instant("api.global.succes.update.title")),this.apiService.getRestartNeeded().subscribe(e=>{e.RestartNeeded&&(this.headerService.setRestart(!0),this.open(this.content))}),this.waiting=!0,setTimeout(()=>{this.getGroups(),this.waiting=!1},1e3)})}delete(e){const t=this.rows.indexOf(e,0);t>-1&&(this.rows.splice(t,1),this.rows=[...this.rows],this.temp=[...this.rows])}add(){const e=new s.b;e.GroupName="",e.coordinatorInside=!1,this.rows.push(e),this.rows=[...this.rows],this.temp=[...this.rows]}updateCoordinator(e,t){t.coordinatorInside=e.currentTarget.checked}open(e){this.modalService.open(e,{ariaLabelledBy:"modal-basic-title"}).result.then(e=>{},e=>{})}isFormValid(){let e=!0;return this.rows.forEach(t=>{t.GroupName&&(t.coordinatorInside||t.devicesSelected&&0!==t.devicesSelected.length)||(e=!1)}),!this.waiting&&e}getGroups(){this.apiService.getZGroups().subscribe(e=>{e&&e.length>0&&(e.forEach(e=>{const t=[];e.coordinatorInside=!1,e.Devices.forEach(c=>{if("0000"===c._NwkId)e.coordinatorInside=!0;else{const e=this.devices.find(e=>e._NwkId===c._NwkId&&e.Ep===c.Ep);null!=e&&t.push(e)}}),e.devicesSelected=t}),this.rows=[...e],this.temp=[...e])})}}return e.\u0275fac=function(t){return new(t||e)(b.Nb(u.e),b.Nb(r.a),b.Nb(n.d),b.Nb(p.d),b.Nb(h.b),b.Nb(l.a))},e.\u0275cmp=b.Hb({type:e,selectors:[["app-group"]],viewQuery:function(e,t){var c;1&e&&(b.Qc(f,!0),b.Qc(w,!0)),2&e&&(b.xc(c=b.fc())&&(t.table=c.first),b.xc(c=b.fc())&&(t.content=c.first))},features:[b.xb],decls:74,vars:30,consts:[[1,"row"],[1,"col-sm-11"],[1,"card"],["translate","group.create.header",1,"card-header"],[1,"card-body"],["translate","group.create.subtitle",1,"card-title"],[1,"card-text"],[1,"col-sm"],["type","text",3,"placeholder","keyup"],[1,"col-sm-2"],["translate","group.create.add.button",1,"w-100","btn","btn-primary",3,"click"],[1,"bootstrap",3,"rows","columnMode","headerHeight","summaryRow","summaryPosition","footerHeight","limit","rowHeight"],["table",""],[3,"maxWidth"],["ngx-datatable-cell-template",""],["prop","_GroupId",3,"maxWidth","name"],["prop","GroupName",3,"maxWidth","name"],[3,"name","sortable"],[3,"maxWidth","name","sortable"],[1,"col-sm-1"],["translate","group.create.validate.button",1,"w-100","btn","btn-primary",3,"disabled","click"],["content",""],[1,"fa","fa-trash",2,"cursor","pointer",3,"title","click"],["autofocus","","type","text",3,"value","change"],["bindLabel","Name","placeholder","Choose device","appendTo","body",3,"items","multiple","closeOnSelect","searchable","ngModel","ngModelChange","change"],["ng-option-tmp",""],[3,"ngOptionHighlight"],[1,"form-check"],["type","checkbox",1,"form-check-input",3,"checked","click"],[1,"modal-header"],["id","modal-basic-title","translate","group.reloadplugin.alert.title",1,"modal-title"],["type","button","aria-label","Close",1,"close",3,"click"],["aria-hidden","true"],["translate","group.reloadplugin.alert.subject",1,"modal-body"],[1,"modal-footer"],["type","button","translate","group.reloadplugin.alert.cancel",1,"btn","btn-outline-dark",3,"click"]],template:function(e,t){1&e&&(b.Tb(0,"div",0),b.Lc(1,"\n  "),b.Tb(2,"div",1),b.Lc(3,"\n    "),b.Tb(4,"div",2),b.Lc(5,"\n      "),b.Ob(6,"div",3),b.Lc(7,"\n      "),b.Tb(8,"div",4),b.Lc(9,"\n        "),b.Ob(10,"h5",5),b.Lc(11,"\n        "),b.Tb(12,"div",6),b.Lc(13,"\n          "),b.Tb(14,"div",0),b.Lc(15,"\n            "),b.Tb(16,"div",7),b.Lc(17,"\n              "),b.Tb(18,"input",8),b.ec("keyup",(function(e){return t.updateFilter(e)})),b.jc(19,"translate"),b.Sb(),b.Lc(20,"\n            "),b.Sb(),b.Lc(21,"\n            "),b.Tb(22,"div",9),b.Lc(23,"\n              "),b.Tb(24,"button",10),b.ec("click",(function(){return t.add()})),b.Sb(),b.Lc(25,"\n            "),b.Sb(),b.Lc(26,"\n          "),b.Sb(),b.Lc(27,"\n          "),b.Tb(28,"ngx-datatable",11,12),b.Lc(30,"\n            "),b.Tb(31,"ngx-datatable-column",13),b.Lc(32,"\n              "),b.Jc(33,v,4,3,"ng-template",14),b.Lc(34,"\n            "),b.Sb(),b.Lc(35,"\n\n            "),b.Tb(36,"ngx-datatable-column",15),b.jc(37,"translate"),b.Lc(38,"\n              "),b.Jc(39,S,1,1,"ng-template",14),b.Lc(40,"\n            "),b.Sb(),b.Lc(41,"\n            "),b.Tb(42,"ngx-datatable-column",16),b.jc(43,"translate"),b.Lc(44,"\n              "),b.Jc(45,T,3,1,"ng-template",14),b.Lc(46,"\n            "),b.Sb(),b.Lc(47,"\n            "),b.Tb(48,"ngx-datatable-column",17),b.jc(49,"translate"),b.Lc(50,"\n              "),b.Jc(51,N,6,5,"ng-template",14),b.Lc(52,"\n            "),b.Sb(),b.Lc(53,"\n            "),b.Tb(54,"ngx-datatable-column",18),b.jc(55,"translate"),b.Lc(56,"\n              "),b.Jc(57,I,6,1,"ng-template",14),b.Lc(58,"\n            "),b.Sb(),b.Lc(59,"\n          "),b.Sb(),b.Lc(60,"\n        "),b.Sb(),b.Lc(61,"\n      "),b.Sb(),b.Lc(62,"\n    "),b.Sb(),b.Lc(63,"\n  "),b.Sb(),b.Lc(64,"\n  "),b.Tb(65,"div",19),b.Lc(66,"\n    "),b.Tb(67,"button",20),b.ec("click",(function(){return t.updateDevices()})),b.Sb(),b.Lc(68,"\n  "),b.Sb(),b.Lc(69,"\n"),b.Sb(),b.Lc(70,"\n\n"),b.Jc(71,E,19,0,"ng-template",null,21,b.Kc),b.Lc(73,"\n")),2&e&&(b.Ab(18),b.pc("placeholder",b.kc(19,20,"group.create.placeholder")),b.Ab(10),b.oc("rows",t.rows)("columnMode","force")("headerHeight",40)("summaryRow",!0)("summaryPosition","bottom")("footerHeight",40)("limit",10)("rowHeight","auto"),b.Ab(3),b.oc("maxWidth",100),b.Ab(5),b.pc("name",b.kc(37,22,"group.create.shortid.column")),b.oc("maxWidth",100),b.Ab(6),b.pc("name",b.kc(43,24,"group.create.groupname.column")),b.oc("maxWidth",200),b.Ab(6),b.pc("name",b.kc(49,26,"group.create.devices.column")),b.oc("sortable",!1),b.Ab(6),b.pc("name",b.kc(55,28,"group.create.coordinator.column")),b.oc("maxWidth",150)("sortable",!1),b.Ab(13),b.oc("disabled",!t.isFormValid()))},directives:[p.a,m.c,m.b,m.a,L.a,n.k,n.m,L.c,g.a],pipes:[p.c],styles:[""]}),e})(),data:{title:Object(a.d)("group")}}];let G=(()=>{class e{}return e.\u0275mod=b.Lb({type:e}),e.\u0275inj=b.Kb({factory:function(t){return new(t||e)},providers:[],imports:[[o.i.forChild(y)],o.i]}),e})(),A=(()=>{class e{}return e.\u0275mod=b.Lb({type:e}),e.\u0275inj=b.Kb({factory:function(t){return new(t||e)},imports:[[G,i.a,n.h]]}),e})()}}]);