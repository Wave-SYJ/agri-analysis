<template>
  <v-chart
    autoresize
    :option="rightOptions"
    @select="handleProvinceClick"
    :loading="mapLoading"
  />
</template>

<script>
import * as echarts from "echarts";
import provinceMap from "@/utils/map/province-map.js";
import axios from "axios";
export default {
  data() {
    return {
      mapLoading: false,
      rightOptions: {},
      provinceShowing: null,
    };
  },
  async created() {
    this.mapLoading = true;
    this.chinaData = (await axios.get("/map/china.json")).data;
    echarts.registerMap("china", this.chinaData);
    this.rightOptions = {
      title: {
        text: "全国地图",
      },
      series: [
        {
          type: "map",
          map: "china",
          selectedMode: "single",
        },
      ],
      toolbox: {
        show: true,
        feature: {
          myBackBtn: {
            show: false,
            title: "返回",
            icon: `image://${require("@/assets/images/back.svg")}`,
            onclick: this.handleMapBack,
          },
        },
      },
    };
    this.mapLoading = false;
  },
  methods: {
    async handleProvinceClick({ dataIndexInside: provinceIndex }) {
      if (this.provinceShowing) return;

      this.mapLoading = true;
      this.rightOptions.toolbox.feature.myBackBtn.show = true;
      const provinceName =
        this.chinaData.features[provinceIndex].properties.name;
      this.provinceShowing = provinceName;
      const provinceData = (
        await axios.get(`/map/province/${provinceMap[provinceName]}.json`)
      ).data;
      this.rightOptions.series[0].map = provinceMap[provinceName];
      this.rightOptions.title.text = `${this.provinceShowing}地图`;
      echarts.registerMap(provinceMap[provinceName], provinceData);
      this.mapLoading = false;
    },
    handleMapBack() {
      this.provinceShowing = null;
      this.rightOptions.series[0].map = "china";
      this.rightOptions.title.text = "全国地图";
    },
  },
};
</script>

<style>
</style>