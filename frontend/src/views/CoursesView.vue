<template>

    <div class="container my-5 ">
        <div class="row">
            <div class="col-lg-3"> <CourseFilter @category-updated="filterCourses" /> </div>
            <div class="col-lg-9"> <CourseList :courses="filteredCourses" /> </div>
        </div>
    </div>
</template>


<script>
    import CourseList from '@/components/CourseList.vue';
    import CourseFilter from '@/components/CourseFilter.vue';
    import { courses } from '../temp-data'

    export default {
        name: 'CoursesList',
        components:{
            CourseList,
            CourseFilter
        },
        data(){
            return {
                courses:courses,
                filteredCourses: courses
            }
        },
        methods:{
            filterCourses(selectedCategory){
                if (selectedCategory.length == 0){
                    this.filteredCourses = this.courses
                }
                else{
                    this.filteredCourses = this.courses.filter(course => selectedCategory.includes( course.category_id))
                }
            }
        }
    }
</script>