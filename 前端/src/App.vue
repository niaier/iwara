<template>
  <div id="components-layout-demo-basic">
    <a-layout class='clearfix'>
      <a-layout-header >
        <!-- class='clearfix' -->
        <div id="menu-bar">
          <div class="left">
            <a-menu v-model="current" mode="horizontal">
              <a-menu-item key="home">
                <router-link to="/">Home</router-link>
              </a-menu-item>
              <a-menu-item key="video">
                <router-link :to="{ path:'/video',query:{page:1} }">Video</router-link>
              </a-menu-item>
              <a-menu-item key="love">
                <router-link :to="{ path:'/love',query:{page:1} }">Love</router-link>
              </a-menu-item>
              <a-menu-item key="playlist">
                <router-link :to="{ path:'/playlist',query:{page:1} }">PlatyList</router-link>
              </a-menu-item>
              <a-menu-item id="menu-bar-right">
                <a-button>登录</a-button>
                <a-button>注册</a-button>
              </a-menu-item>
            </a-menu>
          </div>
        </div>
      </a-layout-header>

      <a-layout-content>
        <router-view :key="this.$route.path"></router-view>
      </a-layout-content>
      <a-layout-footer>Footer</a-layout-footer>
    </a-layout>
  </div>

  <!-- header 部分 -->
  <!-- router-view -->

  <!-- footer -->
</template>
<script>
export default {
  name: "App",
  data() {
    return {
      current: ["home"],
    };
  },
};
</script>




<style lang="scss" scope>
@import './css/base.scss';

#components-layout-demo-basic{
  height: 100%;
  .ant-layout{
    height: 100%;
  }

  .ant-layout-header{
    // height: 100%;
  }
  .ant-layout-content{
    height: 100%;
    // height: 1000px;
  }
  .ant-layout-footer{
    // height: 100%;
  }
}


header.ant-layout-header {
  height: auto;
  padding-left: 0;
  padding-right: 0;

  #menu-bar {
    position: relative;

    ul {
      background: #333;
      border: 0;

      #menu-bar-right {
        position: absolute;
        right: 20px;
        width: 200px;
        border-bottom: none;

        button {
          margin: auto 10px;
        }
      }

      a {
        color: #fff;
      }
    }
  }
}
</style>



