from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='Category',method='filter_by_category')  # 1,2,3,4
    
    
    def filter_by_category(self,queryset,name,value):
        ids = value.split(',')   # [1,2,3,4]
        return queryset.filter(category__id__in=ids)