<template>
  <div>
    <p>{{article}}</p>
  </div>
</template>

<script>

import axios from 'axios';

  export default {
    name: 'HelloWorld',

    data: () => ({
      article: ''
    }),
  methods: {
    getArticle() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.article = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getArticle();
  },
  }
</script>
