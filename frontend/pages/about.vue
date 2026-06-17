<template>
    <div class="container mx-auto min-h-80">
        <h1 class="mt-8">About Us</h1>
        <section class="section-1 mt-4">
            <h2>Who We Are</h2>
            <p>HATIL is a fast-growing Global Furniture Brand with customers and connoisseurs around the globe. The brand
                presents an impeccable range of wooden furniture products manufactured from the best-sourced materials and
                with a deft touch of seasoned artisanship.</p>
        </section>
        <section class="section-2 mt-4">
            <h2>Farshid Shakil,
                Founder of H.A. Timber Industries Ltd.</h2>
            <p>HATIL traces its roots to H.A. Timber Industries Ltd, a company established in 1963 by late Al-Haj Habibur
                Rahman. Following his footsteps, HATIL, as a singular furniture brand, came into being under the leadership
                of Selim H. Rahman, a veteran and visionary leader in country’s furniture industry.

                Over the years, HATIL made itself a synonym to Elegant, Contemporary and Affordable furniture collection.
                Outstanding product quality and design backed by unique customer service are a few traits that helped HATIL
                lead being in the front. It’s worth mentioning that to ensure the best possible quality HATIL has been
                practicing Japanese Quality Management Philosophy “Kaizen” since 2007. And, being an environment-sensible
                company.

                All these things contributed in a great way making HATIL a favorite name across markets like US, Canada,
                Australia, Saudi Arabia, Kuwait, UAE, Thailand, Egypt, Russia, Nepal, Bhutan and India. In Bangladesh
                market, HATIL Furniture has been a proud awardee of HSBC-Daily Star Climate Award, 2013 in Green Operation
                Category.</p>
        </section>
        <section class="section-3 mt-4">
            <div class="seb-sec-1">
                <h3>Principle</h3>
                <p>To do Justice and behave Ethically with our Customers, Partners, Insiders and the Communities</p>
            </div>
            <div class="seb-sec-2">
                <h3>Vision</h3>
                <p>To help elevate the lifestyle and living of people in general with our Innovations, Creations and Business Practices</p>
            </div>
            <div class="seb-sec-3">
                <h3>Mission</h3>
                <p>To stay contemporary and contextual being innovative and cutting-edge</p>
            </div>
        </section>
        <section class="section-4 mt-4">
            <h2>Commitment</h2>
            <p>From pushing boundaries to create sustainable designs, to our concept studio, and innovation lab, we love nothing more than unlocking the potential of space. Our commitment is steadfast in ensuring our designs are functional and efficient whilst never undermining aesthetics.
Our goal is a simple one and that is to bridge the gap between what is desired in modern living and what is available in the market.</p>
        </section>
    </div>
</template>

<script setup>
const { data } = await useFetch("/api/products/?name=anything", {
    method: 'POST',
    body: { age: 27 }
});

useHead({
    title: 'Shakil Furniture | about',
    meta: [
        { name: 'description', content: 'Discover the story behind Shakil Furniture – a leading name in exquisite handcrafted furniture. Our journey of passion and craftsmanship brings life to your spaces. Learn about our heritage, skilled artisans, and commitment to creating timeless pieces. Explore our About page and join us in the art of creating bespoke furniture that reflects your style and character.' },
        { name: 'keywords', content: 'Shakil Furniture, handcrafted furniture, bespoke furniture, craftsmanship, heritage, artisans, timeless pieces, custom furniture, living spaces, furniture design' }
    ]
});

</script>

<style scoped></style>