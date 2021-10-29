from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
import re

class MutantViewSet(viewsets.ViewSet):
    def is_mutant(self, request):
        data = request.data
        dna = data['dna']
        print(dna)


    
        length = len(dna[0])
        string = ' '.join(dna)
        diag_steps = re.escape(str(length+1))
        vert_steps = re.escape(str(length))
        diag_inv_steps = re.escape(str(length-1))

        matches = 0
        
        horizontal_pattern = r'([ACTG])(.{0}\1){3}'
        diag_pattern = r'([ACTG])(.{' + diag_steps + r'}\1){3}'
        vert_pattern = r'([ACTG])(.{' + vert_steps  + r'}\1){3}'
        diag_inv_pattern = r'([ACTG])(.{' + diag_inv_steps + r'}\1){3}'
        
        
        list_of_regex = [horizontal_pattern, diag_pattern, vert_pattern, diag_inv_pattern]

        for pattern in list_of_regex:
            regex = re.findall(pattern, string)
            if regex:
                matches += len(regex)
        
        if matches > 1:
            return Response(status=status.HTTP_200_OK)

        
        elif matches < 2:
            return Response(status=status-status.HTTP_403_FORBIDDEN)

