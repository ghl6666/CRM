from nbapp import models

def pagenation(base_url,current_page_num,total_counts,per_page_counts=10,page_number=5):
    '''
    total_counts数据总数
    per_page_counts每页分多少条数据
    page_number = 页码显示多少个
    current_page_num 当前页
    :return:
    '''
    # all_objs_list = models.Customer.objects.all()
    # total_counts = all_objs_list.count()
    per_page_counts = 10
    # page_number = 5

    try:
        current_page_num = int(current_page_num)

    except Exception:
        current_page_num = 1


    half_page_range = page_number//2
    #计算总页数
    page_number_count,a = divmod(total_counts,per_page_counts)
    if current_page_num < 1:
        current_page_num = 1


    if a:
        page_number_count += 1
    if current_page_num > page_number_count:
        current_page_num = page_number_count

    start_num = (current_page_num - 1) * 10
    end_num = current_page_num * 10

    if page_number_count <= page_number:
        page_start = 1
        page_end = page_number_count
    else:
        if current_page_num <= half_page_range:
            page_start = 1
            page_end = page_number
        elif current_page_num + half_page_range  >= page_number_count:
            page_start = page_number_count - page_number + 1
            page_end = page_number_count
        else:
            page_start = current_page_num - half_page_range
            page_end = current_page_num + half_page_range


    '''
        <nav aria-label="Page navigation">
          <ul class="pagination">
            <li>
              <a href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            <>
            <li><a href="#">1</a><>
            <li><a href="#">2</a><>
            <li><a href="#">3</a><>
            <li><a href="#">4</a><>
            <li><a href="#">5</a><>
            <li>
              <a href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            <>
          </ul>
        </nav>
    '''

    tab_html = ''
    tab_html += '<nav aria-label="Page navigation"><ul class="pagination">'

    #上一页
    if current_page_num == 1:
        previous_page = '<li disabled><a href="#" aria-label="Previous" ><span aria-hidden="true">&laquo;</span></a><>'
    else:
        previous_page = '<li><a href="{0}?page={1}" aria-label="Previous" ><span aria-hidden="true">&laquo;</span></a><>'.format(base_url,current_page_num-1)
    tab_html += previous_page

    for i in range(page_start,page_end+1):
        if current_page_num == i:

            one_tag = '<li class="active"><a href="{0}?page={1}">{1}</a><>'.format(base_url,i)
        else:
            one_tag = '<li><a href="{0}?page={1}">{1}</a><>'.format(base_url, i)
        tab_html += one_tag


    #下一页
    if current_page_num == page_number_count:
        next_page = '<li disabled><a href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a><>'
    else:
        next_page = '<li><a href="{0}?page={1}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a><>'.format(base_url,current_page_num+1)
    tab_html+=next_page
    tab_html += '</ul></nav>'

    return tab_html,start_num,end_num
