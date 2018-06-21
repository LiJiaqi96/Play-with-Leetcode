class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if((C-A)*(D-B) == 0 or (G-E)*(H-F) == 0):
            repeat_area = 0
        else:
            if(E-C>=0):
                line1 = 0
            elif(A-G>=0):
                line1 = 0
            elif((E-A>=0)and(E-C<0)and(G-C>=0)):
                line1 = C - E
            elif((G-C<=0)and(G-A>0)and(E-A<=0)):
                line1 = G - A
            elif((G-C>=0)and(E-A<=0)):
                line1 = C - A
            else:
                line1 = G - E
            if(B-H>=0):
                line2 = 0
            elif(F-D>=0):
                line2 = 0
            elif((H-B>0)and(H-D<=0)and(F-B<=0)):
                line2 = H - B
            elif((F-D<0)and(H-D>=0)and(F-B>=0)):
                line2 = D - F
            elif((H-D>=0)and(F-B<=0)):
                line2 = D - B
            else:
                line2 = H - F
            repeat_area = line1 * line2
        cover_area = (C-A)*(D-B) + (G-E)*(H-F) - repeat_area
        return cover_area
