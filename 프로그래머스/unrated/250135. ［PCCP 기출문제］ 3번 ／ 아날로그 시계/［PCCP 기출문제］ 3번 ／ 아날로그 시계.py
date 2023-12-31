def solution(h1, m1, s1, h2, m2, s2):
    def get_count(h, m, s):
        m_count = h * 59 + m
        h_count = h * 60 + m

        result = -1

        cur_m_degree = m * 6
        cur_h_degree = 30 * (h % 12) + 0.5 * m

        if cur_m_degree <= 5.9 * s:
            m_count += 1
        
        if cur_h_degree <= (6 - 1 / 120) * s:
            h_count += 1
        
        if h >= 12:
            h_count -= 1
            result -= 1

        return result + m_count + h_count

    answer = get_count(h2, m2, s2) - get_count(h1, m1, s1)
    return answer + (s1 == 0 and m1 == 0)
