<!-- 组件说明 -->
<template>
  <div class="left-menu">
    <a-menu
      mode="inline"
      :open-keys="openKeys"
      style="width: 256px"
      @openChange="onOpenChange"
    >
      <a-sub-menu key="sub1">
        <span slot="title">
          <a-icon type="unordered-list" />
          <span>我的播放列表</span>
        </span>
        <a-menu-item
          @click="selectPlayList(v)"
          v-for="(v, i) in playlist"
          :key="i"
          >
            {{ v.playListName }}
          </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </div>
</template>

<script>
//import x from ''
import axios from "axios";
export default {
  components: {},
  data() {
    return {
      rootSubmenuKeys: ["sub1", "sub2", "sub4"],
      openKeys: ["sub1"],
      playlist: "",
    };
  },
  created() {
    this.getApi();
  },
  computed: {},
  methods: {
    onOpenChange(openKeys) {
      const latestOpenKey = openKeys.find(
        (key) => this.openKeys.indexOf(key) === -1
      );
      if (this.rootSubmenuKeys.indexOf(latestOpenKey) === -1) {
        this.openKeys = openKeys;
      } else {
        this.openKeys = latestOpenKey ? [latestOpenKey] : [];
      }
    },
    getApi() {
      let _this = this;

      axios.get("playlist").then((value) => {
        _this.playlist = value.data;
      });
    },
    selectPlayList(v) {
      let query = this.$route.query;
      let page = 1;
      let love_level = query.love_level;
      let sortby = query.sortby;
      let playListId = v.playListId;
      this.$store.commit("getPlayListId", playListId);

      this.$router.push({
        path: "",
        query: {
          page: page,
          love_level,
          sortby,
          playListId,
        },
      });
    },
  },
};
</script>

<style lang='scss' scoped>
//@import url()
</style>