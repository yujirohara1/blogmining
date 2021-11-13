var TODOHUKEN = { 
    hokkaido  :"北海道"   , aomori    :"青森県"   , iwate     :"岩手県"   , miyagi    :"宮城県"    ,
    akita     :"秋田県"   , yamagata  :"山形県"   , fukushima :"福島県"   , ibaraki   :"茨城県"    ,
    tochigi   :"栃木県"   , gunma     :"群馬県"   , saitama   :"埼玉県"   , chiba     :"千葉県"    ,
    tokyo     :"東京都"   , kanagawa  :"神奈川県" , niigata   :"新潟県"   , toyama    :"富山県"    ,
    ishikawa  :"石川県"   , fukui     :"福井県"   , yamanashi :"山梨県"   , nagano    :"長野県"    ,
    gifu      :"岐阜県"   , shizuoka  :"静岡県"   , aichi     :"愛知県"   , mie       :"三重県"    ,
    shiga     :"滋賀県"   , kyoto     :"京都府"   , osaka     :"大阪府"   , hyogo     :"兵庫県"    ,
    nara      :"奈良県"   , wakayama  :"和歌山県" , tottori   :"鳥取県"   , shimane   :"島根県"    ,
    okayama   :"岡山県"   , hiroshima :"広島県"   , yamaguchi :"山口県"   , tokushima :"徳島県"    ,
    kagawa    :"香川県"   , ehime     :"愛媛県"   , kochi     :"高知県"   , fukuoka   :"福岡県"    ,
    saga      :"佐賀県"   , nagasaki  :"長崎県"   , kumamoto  :"熊本県"   , oita      :"大分県"    ,
    miyazaki  :"宮崎県"   , kagoshima :"鹿児島県" , okinawa   :"沖縄県"}  ;


function createAreaMap(){
    
    $('#tblAreaMap tbody').html("");
    for(var i = 1; i <= 12; i++){
        var trid = "tblAreaMapTr_" + i;
        $('#tblAreaMap tbody').append('<tr id="' + trid + '">');
        for(var j = 1; j <= 13; j++){
            var tdid = "tblAreaMapTd_" + i + "_" + j;
            $('#tblAreaMap #' + trid).append('<td id="' + tdid + '">');
        }
    }

    $('#tblAreaMap #tblAreaMapTd_1_12').append('<a href="#">北');
    $('#tblAreaMap #tblAreaMapTd_1_12').addClass("hokkaido");
    $('#tblAreaMap #tblAreaMapTd_1_12').attr("colspan","2");
    $('#tblAreaMap #tblAreaMapTd_1_12').attr("rowspan","2");
    $('#tblAreaMap #tblAreaMapTd_1_13').remove();
    $('#tblAreaMap #tblAreaMapTd_2_12').remove();
    $('#tblAreaMap #tblAreaMapTd_2_13').remove();
    
    $('#tblAreaMap #tblAreaMapTd_3_12').append('<a href="#">青');
    $('#tblAreaMap #tblAreaMapTd_3_12').addClass("tohoku");
    $('#tblAreaMap #tblAreaMapTd_3_12').addClass("aomori");
    $('#tblAreaMap #tblAreaMapTd_3_12').attr("colspan","2");
    $('#tblAreaMap #tblAreaMapTd_3_13').remove();
    
    $('#tblAreaMap #tblAreaMapTd_4_12').append('<a href="#">秋');
    $('#tblAreaMap #tblAreaMapTd_4_12').addClass("tohoku");
    $('#tblAreaMap #tblAreaMapTd_4_12').addClass("akita");
    $('#tblAreaMap #tblAreaMapTd_4_13').append('<a href="#">岩');
    $('#tblAreaMap #tblAreaMapTd_4_13').addClass("tohoku");
    $('#tblAreaMap #tblAreaMapTd_4_13').addClass("iwate");
    $('#tblAreaMap #tblAreaMapTd_5_12').append('<a href="#">山');
    $('#tblAreaMap #tblAreaMapTd_5_12').addClass("tohoku");
    $('#tblAreaMap #tblAreaMapTd_5_12').addClass("yamagata");
    $('#tblAreaMap #tblAreaMapTd_5_13').append('<a href="#">宮');
    $('#tblAreaMap #tblAreaMapTd_5_13').addClass("tohoku");
    $('#tblAreaMap #tblAreaMapTd_5_13').addClass("miyagi");
    
    $('#tblAreaMap #tblAreaMapTd_6_9').append('<a href="#">石');
    $('#tblAreaMap #tblAreaMapTd_6_9').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_6_9').addClass("ishikawa");
    $('#tblAreaMap #tblAreaMapTd_6_10').append('<a href="#">富');
    $('#tblAreaMap #tblAreaMapTd_6_10').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_6_10').addClass("toyama");
    $('#tblAreaMap #tblAreaMapTd_6_11').append('<a href="#">新');
    $('#tblAreaMap #tblAreaMapTd_6_11').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_6_11').addClass("niigata");
    $('#tblAreaMap #tblAreaMapTd_6_12').append('<a href="#">福');
    $('#tblAreaMap #tblAreaMapTd_6_12').addClass("tohoku");
    $('#tblAreaMap #tblAreaMapTd_6_12').addClass("fukushima");
    $('#tblAreaMap #tblAreaMapTd_6_12').attr("colspan","2");
    $('#tblAreaMap #tblAreaMapTd_6_13').remove();

    //
    
    $('#tblAreaMap #tblAreaMapTd_7_9').append('<a href="#">福');
    $('#tblAreaMap #tblAreaMapTd_7_9').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_7_9').addClass("fukui");
    $('#tblAreaMap #tblAreaMapTd_7_10').append('<a href="#">岐');
    $('#tblAreaMap #tblAreaMapTd_7_10').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_7_10').addClass("gifu");
    $('#tblAreaMap #tblAreaMapTd_7_10').attr("rowspan","2");
    $('#tblAreaMap #tblAreaMapTd_8_10').remove();
    $('#tblAreaMap #tblAreaMapTd_7_11').append('<a href="#">長');
    $('#tblAreaMap #tblAreaMapTd_7_11').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_7_11').addClass("nagano");
    $('#tblAreaMap #tblAreaMapTd_7_11').attr("rowspan","2");
    $('#tblAreaMap #tblAreaMapTd_8_11').remove();
    $('#tblAreaMap #tblAreaMapTd_7_12').append('<a href="#">群');
    $('#tblAreaMap #tblAreaMapTd_7_12').addClass("kanto");
    $('#tblAreaMap #tblAreaMapTd_7_12').addClass("gunma");
    $('#tblAreaMap #tblAreaMapTd_7_13').append('<a href="#">栃');
    $('#tblAreaMap #tblAreaMapTd_7_13').addClass("kanto");
    $('#tblAreaMap #tblAreaMapTd_7_13').addClass("tochigi");

    
    $('#tblAreaMap #tblAreaMapTd_8_1').append('<a href="#">佐');
    $('#tblAreaMap #tblAreaMapTd_8_1').addClass("kyushu");
    $('#tblAreaMap #tblAreaMapTd_8_1').addClass("saga");
    $('#tblAreaMap #tblAreaMapTd_8_2').append('<a href="#">福');
    $('#tblAreaMap #tblAreaMapTd_8_2').addClass("kyushu");
    $('#tblAreaMap #tblAreaMapTd_8_2').addClass("fukuoka");
    $('#tblAreaMap #tblAreaMapTd_8_3').append('<a href="#">大');
    $('#tblAreaMap #tblAreaMapTd_8_3').addClass("kyushu");
    $('#tblAreaMap #tblAreaMapTd_8_3').addClass("oita");
    $('#tblAreaMap #tblAreaMapTd_8_4').append('<a href="#">山');
    $('#tblAreaMap #tblAreaMapTd_8_4').addClass("chugoku");
    $('#tblAreaMap #tblAreaMapTd_8_4').addClass("yamaguchi");
    $('#tblAreaMap #tblAreaMapTd_8_4').attr("rowspan","2");
    $('#tblAreaMap #tblAreaMapTd_9_4').remove();
    $('#tblAreaMap #tblAreaMapTd_8_5').append('<a href="#">島');
    $('#tblAreaMap #tblAreaMapTd_8_5').addClass("chugoku");
    $('#tblAreaMap #tblAreaMapTd_8_5').addClass("shimane");
    $('#tblAreaMap #tblAreaMapTd_8_6').append('<a href="#">鳥');
    $('#tblAreaMap #tblAreaMapTd_8_6').addClass("chugoku");
    $('#tblAreaMap #tblAreaMapTd_8_6').addClass("tottori");
    $('#tblAreaMap #tblAreaMapTd_8_7').append('<a href="#">兵');
    $('#tblAreaMap #tblAreaMapTd_8_7').addClass("kinki");
    $('#tblAreaMap #tblAreaMapTd_8_7').addClass("hyogo");
    $('#tblAreaMap #tblAreaMapTd_8_8').append('<a href="#">京');
    $('#tblAreaMap #tblAreaMapTd_8_8').addClass("kinki");
    $('#tblAreaMap #tblAreaMapTd_8_8').addClass("kyoto");
    $('#tblAreaMap #tblAreaMapTd_8_9').append('<a href="#">滋');
    $('#tblAreaMap #tblAreaMapTd_8_9').addClass("kinki");
    $('#tblAreaMap #tblAreaMapTd_8_9').addClass("shiga");
    
    $('#tblAreaMap #tblAreaMapTd_8_12').append('<a href="#">埼');
    $('#tblAreaMap #tblAreaMapTd_8_12').addClass("kanto");
    $('#tblAreaMap #tblAreaMapTd_8_12').addClass("saitama");
    $('#tblAreaMap #tblAreaMapTd_8_13').append('<a href="#">茨');
    $('#tblAreaMap #tblAreaMapTd_8_13').addClass("kanto");
    $('#tblAreaMap #tblAreaMapTd_8_13').addClass("ibaraki");

    
    $('#tblAreaMap #tblAreaMapTd_9_1').append('<a href="#">長');
    $('#tblAreaMap #tblAreaMapTd_9_1').addClass("kyushu");
    $('#tblAreaMap #tblAreaMapTd_9_1').addClass("nagasaki");
    $('#tblAreaMap #tblAreaMapTd_9_2').append('<a href="#">熊');
    $('#tblAreaMap #tblAreaMapTd_9_2').addClass("kyushu");
    $('#tblAreaMap #tblAreaMapTd_9_2').addClass("kumamoto");
    $('#tblAreaMap #tblAreaMapTd_9_2').attr("rowspan","2");
    $('#tblAreaMap #tblAreaMapTd_10_2').remove();
    $('#tblAreaMap #tblAreaMapTd_9_3').append('<a href="#">宮');
    $('#tblAreaMap #tblAreaMapTd_9_3').addClass("kyushu");
    $('#tblAreaMap #tblAreaMapTd_9_3').addClass("miyazaki");
    $('#tblAreaMap #tblAreaMapTd_9_3').attr("rowspan","2");
    $('#tblAreaMap #tblAreaMapTd_10_3').remove();
    $('#tblAreaMap #tblAreaMapTd_9_5').append('<a href="#">広');
    $('#tblAreaMap #tblAreaMapTd_9_5').addClass("chugoku");
    $('#tblAreaMap #tblAreaMapTd_9_5').addClass("hiroshima");
    $('#tblAreaMap #tblAreaMapTd_9_6').append('<a href="#">岡');
    $('#tblAreaMap #tblAreaMapTd_9_6').addClass("chugoku");
    $('#tblAreaMap #tblAreaMapTd_9_6').addClass("okayama");
    $('#tblAreaMap #tblAreaMapTd_9_7').append('<a href="#">大');
    $('#tblAreaMap #tblAreaMapTd_9_7').addClass("kinki");
    $('#tblAreaMap #tblAreaMapTd_9_7').addClass("osaka");
    $('#tblAreaMap #tblAreaMapTd_9_8').append('<a href="#">奈');
    $('#tblAreaMap #tblAreaMapTd_9_8').addClass("kinki");
    $('#tblAreaMap #tblAreaMapTd_9_8').addClass("nara");
    $('#tblAreaMap #tblAreaMapTd_9_9').append('<a href="#">三');
    $('#tblAreaMap #tblAreaMapTd_9_9').addClass("kinki");
    $('#tblAreaMap #tblAreaMapTd_9_9').addClass("mie");
    
    $('#tblAreaMap #tblAreaMapTd_9_10').append('<a href="#">愛');
    $('#tblAreaMap #tblAreaMapTd_9_10').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_9_10').addClass("aichi");
    $('#tblAreaMap #tblAreaMapTd_9_11').append('<a href="#">山');
    $('#tblAreaMap #tblAreaMapTd_9_11').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_9_11').addClass("yamanashi");
    
    $('#tblAreaMap #tblAreaMapTd_9_12').append('<a href="#">東');
    $('#tblAreaMap #tblAreaMapTd_9_12').addClass("kanto");
    $('#tblAreaMap #tblAreaMapTd_9_12').addClass("tokyo");
    $('#tblAreaMap #tblAreaMapTd_9_13').append('<a href="#">千');
    $('#tblAreaMap #tblAreaMapTd_9_13').addClass("kanto");
    $('#tblAreaMap #tblAreaMapTd_9_13').addClass("chiba");
    $('#tblAreaMap #tblAreaMapTd_9_13').attr("rowspan","2");
    $('#tblAreaMap #tblAreaMapTd_10_13').remove();

    $('#tblAreaMap #tblAreaMapTd_10_4').append('<a href="#">愛');
    $('#tblAreaMap #tblAreaMapTd_10_4').addClass("shikoku");
    $('#tblAreaMap #tblAreaMapTd_10_4').addClass("ehime");
    $('#tblAreaMap #tblAreaMapTd_10_5').append('<a href="#">香');
    $('#tblAreaMap #tblAreaMapTd_10_5').addClass("shikoku");
    $('#tblAreaMap #tblAreaMapTd_10_5').addClass("kagawa");
    $('#tblAreaMap #tblAreaMapTd_10_7').append('<a href="#">和');
    $('#tblAreaMap #tblAreaMapTd_10_7').addClass("kinki");
    $('#tblAreaMap #tblAreaMapTd_10_7').addClass("wakayama");
    $('#tblAreaMap #tblAreaMapTd_10_7').attr("colspan","2");
    $('#tblAreaMap #tblAreaMapTd_10_8').remove();
    $('#tblAreaMap #tblAreaMapTd_10_11').append('<a href="#">静');
    $('#tblAreaMap #tblAreaMapTd_10_11').addClass("chubu");
    $('#tblAreaMap #tblAreaMapTd_10_11').addClass("shizuoka");
    
    $('#tblAreaMap #tblAreaMapTd_10_12').append('<a href="#">神');
    $('#tblAreaMap #tblAreaMapTd_10_12').addClass("kanto");
    $('#tblAreaMap #tblAreaMapTd_10_12').addClass("kanagawa");
    
    $('#tblAreaMap #tblAreaMapTd_11_1').append('<a href="#">沖');
    $('#tblAreaMap #tblAreaMapTd_11_1').addClass("okinawa");
    $('#tblAreaMap #tblAreaMapTd_11_2').append('<a href="#">鹿');
    $('#tblAreaMap #tblAreaMapTd_11_2').addClass("kyushu");
    $('#tblAreaMap #tblAreaMapTd_11_2').addClass("kagoshima");
    $('#tblAreaMap #tblAreaMapTd_11_2').attr("colspan","2");
    $('#tblAreaMap #tblAreaMapTd_11_3').remove();
    $('#tblAreaMap #tblAreaMapTd_11_4').append('<a href="#">高');
    $('#tblAreaMap #tblAreaMapTd_11_4').addClass("shikoku");
    $('#tblAreaMap #tblAreaMapTd_11_4').addClass("kochi");
    $('#tblAreaMap #tblAreaMapTd_11_5').append('<a href="#">徳');
    $('#tblAreaMap #tblAreaMapTd_11_5').addClass("shikoku");
    $('#tblAreaMap #tblAreaMapTd_11_5').addClass("tokushima");
    //1 <td class="hokkaido" colspan="2" rowspan="2"><a href="#">北</a></td>
    //3 <td class="tohoku" colspan="2"><a href="#">青</a></td>

    //$('#tblAreaMap #tblAreaMapTd_11_1').addClass("tdfk_flash");
    //$('#tblAreaMap #tblAreaMapTd_1_12').addClass("tdfk_flash");
    //$('#tblAreaMap #tblAreaMapTd_6_11').addClass("tdfk_flash");
    //$('#tblAreaMap #tblAreaMapTd_7_11').addClass("tdfk_flash");

    for(var i=2; i<=6; i++){
        $('#tblAreaMap #tblAreaMapTd_' + i + '_1').attr("colspan","7");
        for(var j=2; j<=7; j++){
            $('#tblAreaMap #tblAreaMapTd_' + i + '_' + j).remove();
        }
    }

}