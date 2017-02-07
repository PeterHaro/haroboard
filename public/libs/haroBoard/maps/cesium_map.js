var cesiumWidget = new Cesium.Viewer("cesiumContainer", {
    imageryProvider: false,
    baseLayerPicker: false
});
var baselayerInjector = new CesiumBaseLayerInjection();
baselayerInjector.init();
var layers = cesiumWidget.scene.imageryLayers;

var baseLayerPicker = new Cesium.BaseLayerPicker("baseLayerPickerContainer", {
    globe: cesiumWidget.scene,
    imageryProviderViewModels:  baselayerInjector.getImageryViewModels(),
    terrainProviderViewModels: baselayerInjector.getTerrainProviders()
});

$('.cesium-baseLayerPicker-item').each(function () {
    var label = $(this).find($('.cesium-baseLayerPicker-itemLabel'));
    var baseLayerId = encodeURIComponent(label.html());
    $(this).prop('id', baseLayerId);
});