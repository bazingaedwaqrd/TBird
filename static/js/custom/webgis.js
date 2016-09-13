/**
* Created by Edward on 2016/8/20.
*/
$(function() {
    //参数设置
    var setup = {
        //唐山坐标范围
        'MapCenter': [118.31, 39.5],
        'MapZoom': 9,
        'MapProjection': "EPSG:4326",//经纬度网格
    }
    var vector = new ol.layer.Heatmap({
        source: new ol.source.Vector({
            url: 'static/tmp/test.geojson',
            format: new ol.format.GeoJSON(),
        }),
        radius: 8,
        blur: 5,
    });

    var raster = new ol.layer.Tile({
        source: new ol.source.OSM()
    });

    var map = new ol.Map({
        controls: ol.control.defaults().extend([
            new ol.control.FullScreen(),
            new ol.control.ScaleLine(),
        ]),
        layers: [raster],
        target: 'map',
        view: new ol.View({
            center: setup['MapCenter'],
            zoom: setup['MapZoom'],
            projection: setup['MapProjection'],
        })
    });

    function getContentHeight() {
        var viewHeight = $(window).height();
        var menu = $(".bc-menu:visible:visible");
        return viewHeight - menu.outerHeight();
    }

    map.setSize([$(window).width(), getContentHeight()]);
});