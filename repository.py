
import pymysql
import logging as log

def create_connection():
    conn_prod = pymysql.connect(host='172.30.1.66', user='jelly', password='Jellynice1!', port=3307, db='everytimer_prod')
    return conn_prod

def get_category_template(category, first_p, last_p):
    conn_prod = create_connection()

    try:
        with conn_prod.cursor() as cursor:
            first_page = (int(first_p) - 1) * 10
            last_page = (int(last_p) - 1) * 10

            cursor.execute(
                'SELECT name,hours,minutes,seconds,category,temp_id,img FROM category_template WHERE category=%s ORDER BY name ASC LIMIT %s,%s',
                (category,first_page, last_page))
            tmp_fetch = cursor.fetchall()
            category_temp_list = [list(tmp_fetch[x]) for x in range(len(tmp_fetch))]

            print(len(tmp_fetch),tmp_fetch)

            for i in range(len(category_temp_list)):
                tmp_data = category_temp_list[i]
                category_temp_list[i] = dict()
                category_temp_list[i]['name'] = tmp_data[0]
                category_temp_list[i]['hours'] = tmp_data[1]
                category_temp_list[i]['minutes'] = tmp_data[2]
                category_temp_list[i]['seconds'] = tmp_data[3]
                category_temp_list[i]['category'] = tmp_data[4]
                category_temp_list[i]['temp_id'] = tmp_data[5]
                category_temp_list[i]['img'] = tmp_data[6]

            print(f"카테고리 템플릿 가져오기 성공 : [{category_temp_list}]")
            log.info(f"카테고리 템플릿 가져오기 성공 : [{category_temp_list}]")

            return category_temp_list
    except Exception as e:
        log.error(f"===카테고리 데이터 가져오기 실패 :  [{e}]===")
    finally:
        conn_prod.close()

if __name__ == '__main__':
    get_category_template('study',1,2)
