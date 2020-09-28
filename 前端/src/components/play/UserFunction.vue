<!-- 组件说明 -->
<template>
  <div class = 'user-function'>
    <a-row class='clearfix'>
      <a-col
        :xs="{ span: 22, offset: 1 }"
        :lg="{ span: 18, offset: 3 }"
        :xl="{ span: 16, offset: 4 }"
        class="video-info"
      >
        <!-- <a-button>Like</a-button> -->
        <div id="components-dropdown-demo-placement">
          <!-- 喜爱功能 -->
          <a-dropdown :trigger="['click']">
            <a-menu
              slot="overlay"
              @click="handleMenuClick"
              :placement="placement"
              class="placement"
            >
              <a-menu-item :key="'0'" class="love-color-0">
                <a-icon type="heart" />&nbsp;不喜爱
              </a-menu-item>
              <a-menu-item
                v-for="count in 9"
                :key="count"
                :class="'love-color-'+count"
                @click="addLove(count)"
              >
                <a-icon type="heart" />
                喜爱级别{{count}}
              </a-menu-item>
            </a-menu>
            <a-button style="margin-left: 8px" :class="'love-color-'+love_level">
              <a-icon type="heart" theme="filled" v-show="!love_level" />
              <a-icon type="heart" v-show="love_level" />Like
              <!-- <a-icon type="down" /> -->
            </a-button>
          </a-dropdown>
          <!-- 播放列表功能 -->
          <a-dropdown :trigger="['click']">
            <a-menu
              slot="overlay"
              @click="handleMenuClickPlayList"
              :placement="placement"
              class="placement"
            >
              <a-menu-item v-for="(v,i) in playList" :key="i">
                <a-checkbox
                  @click.stop
                  @click="addMyPlayList($event,v)"
                  :checked="checkBox(v,i)"
                  @change="onChange"
                >{{v.playListName}}</a-checkbox>
                <!-- 删除列表 -->
                <a-button
                  type="primary"
                  class="playlist-delete"
                  icon="close"
                  size="small"
                  @click.stop
                  @click="deletePlayList(v)"
                ></a-button>
              </a-menu-item>
              <!-- 输入框 -->
              <a-menu-item>
                <a-input
                  @click.stop
                  key="inputPlayList"
                  v-model="inputPlayListName"
                  placeholder="输入列表名"
                />
                <!-- <input @click.stop="a" /> -->
              </a-menu-item>
              <a-menu-item>
                <a-button
                  @click.stop
                  @click="addPlayList(inputPlayListName)"
                  style="margin-left: 0px"
                >
                  <a-icon type="plus" />添加列表
                </a-button>
              </a-menu-item>
            </a-menu>
            <a-button style="margin-left: 8px">
              PlayList
              <!-- <a-icon type="down" /> -->
            </a-button>
          </a-dropdown>

          <!-- 关注 -->
          <a-button>Follow</a-button>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "UserFunction",
  components: {},
  data() {
    return {
      placement: "bottomRight",
      love_level: "",
      heratFlag: "",
      playList: "",
      myPlayList: "",
      isPlayListChecked: false,
      inputPlayListName: "",
    };
  },
  computed: {},
  methods: {
    handleButtonClick(e) {
      console.log("click left button", e);
    },
    handleMenuClick(e) {
      console.log("click", e);
      let dirname = this.$route.params.videoId;
      axios
        .get(
          "video/" + dirname + "/loved?add=" + e.key
        )
        .then((value) => {
          console.log(value);
        });
      this.getApi();
    },
    a(e) {
      console.log("a");
      e.stopPropagation();
    },
    handleMenuClickPlayList(e) {
      console.log("click", e);
      // e.stopPropagation();
      // e.stopPropagation();
    },
    onChange(e) {
      console.log(`checked = ${e.target.checked}`);
      // checked此状态
    },
    getApi() {
      let _this = this;
      let dirname = _this.$route.params.videoId;
      axios
        .get("video/" + dirname + "/loadLoveList")
        .then((value) => {
          console.log(value);
          _this.love_level = value.data.love_level;
          console.log("love_level", _this.love_level);
          return axios.get(
            "video/" + dirname + "/loadMyPlayList"
          );
        })
        .then((value) => {
          console.log(value);
          // _this.love_level = value.data.love_level;
          _this.myPlayList = value.data;
          return axios.get(
            "video/" + dirname + "/loadPlayList"
          );
        })
        .then((value) => {
          console.log(value);
          _this.playList = value.data;
        });
    },
    addLove(count) {
      console.log(count);
      let _this = this;
      let dirname = this.$route.params.videoId;
      axios
        .get(
          "video/" + dirname + "/loved?add=" + count
        )
        .then((value) => {
          console.log(value);
        });
      _this.getApi();
    },
    addPlayList(playListName) {
      console.log(playListName);
      let _this = this;
      let dirname = this.$route.params.videoId;
      axios
        .get(
          "video/" +
            dirname +
            "/addlist?addName=" +
            playListName
        )
        .then((value) => {
          console.log(value);
        });
      _this.getApi();
    },
    addMyPlayList($event, v) {
      console.log(v.playListId);
      let _this = this;
      let dirname = this.$route.params.videoId;
      axios
        .get(
          "video/" +
            dirname +
            "/addMYlist?isMylist=" +
            $event.target.checked +
            "&playListId=" +
            v.playListId
        )
        .then((value) => {
          console.log(value);
        });
      _this.getApi();
    },
    deletePlayList(v) {
      console.log("vvvvvvvvvvv", v);

      let _this = this;
      let id = v.playListId;
      let dirname = this.$route.params.videoId;
      axios
        .get(
          "video/" +
            dirname +
            "/deletlist?deletPlayListId=" +
            id
        )
        .then((value) => {
          console.log(value);
        });
      _this.getApi();
    },
    checkBox(v, i) {
      // let _this=this;
      for (let index in this.myPlayList) {
        if (v.playListId == this.myPlayList[index].p_id_playListId) {
          console.log("存在", v.playListId);
          return true;
        }
      }
      console.log(i);
    },
  },
  created() {
    this.getApi();
    // this.checkBox();
  },
};
</script>

<style lang='scss' scoped>
//@import url()

.user-function{
  // height: 1000px;
}


#components-dropdown-demo-placement {
  // position: absolute;
  // left: -10px;
  margin-left: -10px;
}
.ant-btn {
  margin-left: 10px;
}
.placement {
  // position: absolute;
  // bottom: auto;
  //   left: -50%;
}
.playlist-delete.ant-btn-icon-only.ant-btn-sm {
  float: right;
  width: 20px;
  height: 20px;
  padding: 0;
  font-size: 12px;
  border-radius: 2px;
}

// .love-color-0 {
//   // color: white;
//   // background-color: rgb(129, 129, 129) !important;
// }

.love-color-1 {
  color: white;

  background-color: red !important;
}
.love-color-2 {
  color: white;

  background-color: orange !important;
}
.love-color-3 {
  color: white;

  background-color: rgba(197, 197, 45, 1) !important;
}
.love-color-4 {
  color: white;

  background-color: green !important;
}
.love-color-5 {
  color: white;

  background-color: blue !important;
}
.love-color-6 {
  color: white;

  background-color: Indigo !important;
}
.love-color-7 {
  color: white;

  background-color: purple !important;
}
.love-color-8 {
  color: white;

  background-color: pink !important;
}
.love-color-9 {
  color: white;

  background-color: black !important;
}

.check-box {
  border: 1px solid black;
}
</style>