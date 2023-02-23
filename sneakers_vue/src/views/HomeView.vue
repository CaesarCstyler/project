<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to ArnalImanShoes
        </p>
        <p class="subtitle">
          The best sneakers store online
        </p>
      </div>
    </section>

    <div class="columns-is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest sneakers</h2>
      </div>

      <div 
        class="column is-3" 
        v-for="sneakers in latestSneakers" 
        v-bind:key="sneakers.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img :src="sneakers.get_thumbnail">
          </figure>

          <h3 class="is-size-4">{{ sneakers.name }}</h3>
          <p class="is-size-6 has-text-grey">${{ sneakers.price }}</p>

          View details
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      latestSneakers: []
    }
  },
  components: {
  },
  mounted() {
    this.getLatestSneakers()
  },
  methods: {
    getLatestSneakers() {
      axios
        .get('/api/v1/latest-sneakers/')
        .then(response => {
          this.latestSneakers = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
