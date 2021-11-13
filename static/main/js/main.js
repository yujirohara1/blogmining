$(document).ready(function() {
    try{
        createMainTable();
    }catch(e){

    }
    return;
});

var autodown = false;
var mainTable = null;
function createMainTable(binddata){
    mainTable = null;
    mainTable = $('#tableJisseki').DataTable({
        bInfo: false,
        bSort: true,
        destroy: true,
        "processing": true,
        columns: [
          { data: 'id'         ,width: '5%',  className: 'dt-body-left'},
          { data: 'tokoDate'    ,width: '10%',  className: 'dt-body-left'},
          { data: 'title'      ,width: '10%',  className: 'dt-body-left'},
          { data: 'category'      ,width: '10%',  className: 'dt-body-left'},
          { data: 'honbun' ,width: '65%' ,  className: 'dt-body-left', render: 
            function (data, type, row) { 
                return data;
            }
          }
        ],
        language: {
           url: "../static/main/js/japanese.json",
        },
        searching: false,
        "pageLength": 1000,
        //"scrollY":$(window).height() * 95 / 100,
        paging:false,
        "order": [ 0, "asc" ],
        "lengthMenu": [100, 300, 500, 1000],
        dom:"<'row'<'col-sm-12'tr>>" +
            "<'row'<'col-sm-6'l><'col-sm-6'f>>"+
            "<'row'<'col-sm-5'i><'col-sm-7'p>>",
      "preDrawCallback": function (settings) {
        return;
      },
      "drawCallback": function (settings) {
          var obj = document.getElementById("tableJisseki");
          if(autodown){
            document.scrollingElement.scrollTop = obj.scrollHeight;
          }
          return;
      }
    });
  }


function insertBlankRow(){
    var tr=$("<tr class='newRow'>");
    var td="";
    td += "<td class='cell-loading' style='color:white'>999999</td>";
    td += "<td class='cell-loading' style='color:white'>999999</td>";
    td += "<td class='cell-loading'>&nbsp;</td>";
    td += "<td class='cell-loading'>&nbsp;</td>";
    td += "<td class='cell-loading'>&nbsp;</td>";
    tr.append(td);
    mainTable.row.add(tr).draw(false);
}

var loopCnt = 0;
function getNextRow(){
    loopCnt += 1;

    $.ajax({
        type: "GET",
        url: "/tryScrapeKiji/" + loopCnt ,
    }).done(function(data) {
        var a = JSON.parse(data).aaData;
        mainTable.row(".newRow").remove().draw();
        if(a.length>0){
            if(a[0].honbun!="" && a[0].title!="" && a[0].tokoDate!=""){
                mainTable.row.add(a[0]).draw(false);
            }
        }

        if(loopCnt < 1000){
            getNextRow();
        } else{
            mainTable.row(".newRow").remove().draw();
            autodown = false;
        }

    }).fail(function(data) {
        alert("エラー：" + data.statusText);
    }).always(function(data) {
        //何もしない
    });
    insertBlankRow();

}
$('#btnRefleshJisseki').click(function() {
    autodown = true;
    getNextRow();
});





