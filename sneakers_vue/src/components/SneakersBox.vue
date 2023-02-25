<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="sneakers.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ sneakers.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ sneakers.price }}</p>

            <router-link v-bind:to="sneakers.get_absolute_url" class="button is-dark mt-4">View details</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SneakersBox',
    props: {
        sneakers: Object
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
